from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="testdb", collection_name="testcollection"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

class FlaskMongoAPI:
    def __init__(self, db_connection):
        self.app = Flask(__name__)
        self.db_connection = db_connection
        self.collection = db_connection.collection
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/create", methods=["POST"])
        def create():
            data = request.json
            if not data:
                return jsonify({"error": "No data provided"}), 400

            inserted = self.collection.insert_one(data)
            return jsonify({"message": "Document created", "id": str(inserted.inserted_id)})

        @self.app.route("/read", methods=["GET"])
        def read_all():
            documents = list(self.collection.find())
            for doc in documents:
                doc["_id"] = str(doc["_id"])
            return jsonify(documents)

        @self.app.route("/read/<id>", methods=["GET"])
        def read_one(id):
            try:
                document = self.collection.find_one({"_id": ObjectId(id)})
                if document:
                    document["_id"] = str(document["_id"])
                    return jsonify(document)
                else:
                    return jsonify({"error": "Document not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

        @self.app.route("/update/<id>", methods=["PUT"])
        def update(id):
            data = request.json
            if not data:
                return jsonify({"error": "No data provided"}), 400

            try:
                result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
                if result.matched_count:
                    return jsonify({"message": "Document updated"})
                else:
                    return jsonify({"error": "Document not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

        @self.app.route("/delete/<id>", methods=["DELETE"])
        def delete(id):
            try:
                result = self.collection.delete_one({"_id": ObjectId(id)})
                if result.deleted_count:
                    return jsonify({"message": "Document deleted"})
                else:
                    return jsonify({"error": "Document not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

    def run(self, debug=True):
        self.app.run(debug=debug)

if __name__ == "__main__":
    db_connection = MongoDBConnection()
    api = FlaskMongoAPI(db_connection)
    api.run()