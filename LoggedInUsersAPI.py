from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib
import uuid

class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="ecommerce", collection_name="users"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

class ECommerceUserAPI:
    def __init__(self, db_connection):
        self.app = Flask(__name__)
        self.db_connection = db_connection
        self.collection = db_connection.collection
        self.setup_routes()

    def hash_password(self, password):
        #Hashes a plain-text password using SHA256.
        return hashlib.sha256(password.encode()).hexdigest()

    def setup_routes(self):
        @self.app.route("/users", methods=["POST"])
        def create_user():
            #Function for creating a new user.
            data = request.json
            if not all(key in data for key in ["name", "email", "phoneNumber", "password", "role"]):
                return jsonify({"error": "Missing required fields"}), 400

            # Hash the password and generate a token
            data["password"] = self.hash_password(data["password"])
            data["token"] = str(uuid.uuid4())  # Generate a unique session token
            data["active"] = True

            # Insert the user into the database
            inserted = self.collection.insert_one(data)
            return jsonify({"message": "User created", "id": str(inserted.inserted_id)}), 201

        @self.app.route("/users", methods=["GET"])
        def get_all_users():
            #Function for Retrieving all users
            users = list(self.collection.find())
            for user in users:
                user["_id"] = str(user["_id"])
                del user["password"]  # Don't return passwords
            return jsonify(users), 200

        @self.app.route("/users/<id>", methods=["GET"])
        def get_user_by_id(id):
            #Retrieve a user by ID
            try:
                user = self.collection.find_one({"_id": ObjectId(id)})
                if user:
                    user["_id"] = str(user["_id"])
                    del user["password"]  # Don't return passwords
                    return jsonify(user), 200
                else:
                    return jsonify({"error": "User not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

        @self.app.route("/users/<id>", methods=["PUT"])
        def update_user(id):
            # Function for updating an existing user.
            data = request.json
            try:
                # Don't allow updating the token directly
                if "token" in data:
                    del data["token"]

                # Update password if provided
                if "password" in data:
                    data["password"] = self.hash_password(data["password"])

                result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
                if result.matched_count:
                    return jsonify({"message": "User updated"}), 200
                else:
                    return jsonify({"error": "User not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

        @self.app.route("/users/<id>", methods=["DELETE"])
        def delete_user(id):
            #Function for deleting a user
            try:
                result = self.collection.delete_one({"_id": ObjectId(id)})
                if result.deleted_count:
                    return jsonify({"message": "User deleted"}), 200
                else:
                    return jsonify({"error": "User not found"}), 404
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400

    def run(self, debug=True):
        self.app.run(debug=debug)

if __name__ == "__main__":
    db_connection = MongoDBConnection()
    api = ECommerceUserAPI(db_connection)
    api.run()