import pymongo
#One should take keys as JSON
from flask import Flask, request, jsonify

class DatabaseManager:
    def __init__(self):
        self.client = None
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["productDb"]
            self.collection = self.db["product"]
            print("Connected to MongoDB")
        except Exception as e:
            print("Error connecting to MongoDB:", e)

    def insert(self, body):
        # Insert data into the database
        try:
            db_id = self.collection.insert_one(body).inserted_id
            print("Data Inserted. ID is:", db_id)
        except Exception as e:
            print("Error inserting data into the database:", e)

    def read(self, query={}):
        # Read data from the database
        try:
            documents = self.collection.find(query)
            for doc in documents:
                print(doc)
        except Exception as e:
            print("Error reading data from the database:", e)

    def update(self, query, new_values):
        # Update data in the database
        try:
            result = self.collection.update_one(query, {"$set": new_values})
            print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")
        except Exception as e:
            print("Error updating data in the database:", e)

    def delete(self, query):
        # Delete data from the database
        try:
            result = self.collection.delete_one(query)
            print(f"Deleted {result.deleted_count} document(s).")
        except Exception as e:
            print("Error deleting data from the database:", e)

    def __del__(self):
        if self.client is not None:
            self.client.close()
            print("Connection Closed")

def main():
    app = Flask(__name__)

    db = DatabaseManager()
    
    # Insert a document
    product = {
        "name": "Product1",
        "price": 10.99,
    }
    

# Route to handle JSON data
    @app.route('/mongodb-crud-task1', methods=['POST'])
    def handle_json():
        data = request.get_json()  # Parse JSON data
        print(data)

        # Create a entry using POST Request to MongoDB using insert() via pymongo
        db.insert(data)
        return jsonify({
            "message": "MongoDB data inserted successfully!",
            "data": data
        })
        
    db.insert(product)
    
    # Read documents
    print("\nReading documents:")
    db.read()
    
    # Update a document
    print("\nUpdating document:")
    db.update({"name": "Product1"}, {"price": 12.99})
    
    # Read updated documents
    print("\nReading updated documents:")
    db.read({"name": "Product1"})
    
    # Delete a document
    print("\nDeleting document:")
    db.delete({"name": "Product1"})
    
    # Read documents after deletion
    print("\nReading documents after deletion:")
    db.read()
    if __name__ == "__main__":
        app.run(debug=True, port=2202)

main()


