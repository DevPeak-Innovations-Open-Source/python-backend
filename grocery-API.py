from flask import Flask, request, jsonify
import pymongo
from bson import ObjectId

app = Flask(__name__)

class DatabaseManager:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["groceryDb"]
            self.collection = self.db["groceryProducts"]
            print("Connected to MongoDB")
        except Exception as e:
            print("Error connecting to MongoDB:", e)

    def insert_product(self, product):
        try:
            result = self.collection.insert_one(product)
            return str(result.inserted_id)
        except Exception as e:
            return str(e)

    def get_all_products(self):
        try:
            products = list(self.collection.find())
            for product in products:
                product['_id'] = str(product['_id'])
            return products
        except Exception as e:
            return str(e)

    def update_product(self, product_id, updated_data):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(product_id)},
                {"$set": updated_data}
            )
            return result.modified_count > 0
        except Exception as e:
            return str(e)

    def delete_product(self, product_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(product_id)})
            return result.deleted_count > 0
        except Exception as e:
            return str(e)

# Create an instance of DatabaseManager
db_manager = DatabaseManager()

# Routes for CRUD operations
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(db_manager.get_all_products())

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    if "productName" in data and "expiryDate" in data and "price" in data and "image" in data:
        product_id = db_manager.insert_product(data)
        return jsonify({"message": "Product added", "product_id": product_id})
    else:
        return jsonify({"error": "Missing required fields"}), 400

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated = db_manager.update_product(product_id, data)
    if updated:
        return jsonify({"message": "Product updated"})
    else:
        return jsonify({"error": "Failed to update product"}), 400

@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted = db_manager.delete_product(product_id)
    if deleted:
        return jsonify({"message": "Product deleted"})
    else:
        return jsonify({"error": "Failed to delete product"}), 400

if __name__ == '__main__':
    app.run(debug=True)
