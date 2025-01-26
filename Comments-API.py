from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId



# For establishing a connection to the MongoDB Database Server
class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name = "comments_database", collection_name = "comments_collection"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
        
# Defining the API for Comments        
class CommentsAPI:
    def __init__(self, db_connection):
        self.app = Flask(__name__)
        self.db_connection = db_connection
        self.collection = db_connection.collection
        self.setup_routes()
        
    # Setting up CRUD Routes
    def setup_routes(self):
        @self.app.route("/comments", methods=["POST"])
        
        #Function for Commenting or Creating a Comment
        def create_comment():
            data = request.json
            
            if not data or not "commentersName" in data or not "comment" in data:
                return jsonify({"error": "Invalid Input: 'commentersName' and 'comment' is required"}), 400
            
            inserted_comment = self.collection.insert_one(data)
            return jsonify({"message": "Comment Created:" f"id: {str(inserted_comment.inserted_id)}"}), 201
        
        
        #Function for Reading all the Comments
        def read_all_comments():
            
            # For getting the comments in form of a list
            comments = list(self.collection.find())
            for comment in comments:
                comment["_id"] = str(comment["_id"])
                return jsonify(comments), 200
            
        @self.app.route("/comments/<id>", methods=["PUT"])
        
        
        # Function for Updating a Comment By ID
        def update_comment(id):
            data = request.json
            
            if not data or "commentersName" in data or not "comment" in data:
                return jsonify({"error": "Invalid Input: 'commentersName' and 'comment' is required"}), 400
            
            try:
                updated = self.collection.update_one(
                    {"_id": ObjectId(id)}, {"$set": data}
                )
                if updated.match_count:
                    return jsonify({"message": "Comment Updated"}), 200
                else:
                    return jsonify({"error": "Comment not found"}), 404
            
            except Exception:
                return jsonify({"error": "Invalid ID"}), 400
            
        
        # Function for Deleting a Comment By ID
        def delete_comment(id):
            try:
                
                deleted = self.collection.delete_one({"_id": ObjectId(id)})
                
                if deleted.deleted_count:
                    return jsonify({"message": "Comment Deleted"}), 200
                else:
                    return jsonify({"error": "Comment not found"}), 404
                
            except:
                return jsonify({"error": "Invalid ID"}), 400
            
        
        # Run the Flask App
        def run(self, Debug=True):
            self.app.run(debug=Debug)
            
            

if __name__ == "__main__":
    db_connection = MongoDBConnection()
    comments_api = CommentsAPI(db_connection)
    comments_api.run()
        