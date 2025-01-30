import pymongo

class DatabaseManager:
    def __init__(self):
        self.client = None
        try:
            self.client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["eCommerceDb"]
            self.collection = self.db["categories"]
            print("Connected to MongoDB")
        except Exception as e:
            print("Error connecting to MongoDB:", e)

    def insert_category(self, category):
        #Insert category into the database
        try:
            db_id = self.collection.insert_one(category).inserted_id
            print("Category Inserted. ID is:", db_id)
        except Exception as e:
            print("Error inserting category into the database:", e)

    def read_categories(self, query={}):
        #Read categories from the database
        try:
            categories = self.collection.find(query)
            for category in categories:
                print(category)
        except Exception as e:
            print("Error reading categories from the database:", e)

    def update_category(self, query, new_values):
        #Update category in the database
        try:
            result = self.collection.update_one(query, {"$set": new_values})
            print(f"Matched {result.matched_count} category(s) and modified {result.modified_count} category(s).")
        except Exception as e:
            print("Error updating category in the database:", e)

    def delete_category(self, query):
        #Delete category from the database
        try:
            result = self.collection.delete_one(query)
            print(f"Deleted {result.deleted_count} category(s).")
        except Exception as e:
            print("Error deleting category from the database:", e)

    def __del__(self):
        if self.client is not None:
            self.client.close()
            print("Connection Closed")


def main():
    db = DatabaseManager()

    # Insert a category
    category = {
        "categoryName": "Electronics",
        "categoryId": "elec123"
    }
    db.insert_category(category)
    
    # Read categories
    print("\nReading categories:")
    db.read_categories()

    # Update a category
    print("\nUpdating category:")
    db.update_category({"categoryId": "elec123"}, {"categoryName": "Home Electronics"})
    
    # Read updated categories
    print("\nReading updated categories:")
    db.read_categories({"categoryId": "elec123"})
    
    # Delete a category
    print("\nDeleting category:")
    db.delete_category({"categoryId": "elec123"})
    
    # Read categories after deletion
    print("\nReading categories after deletion:")
    db.read_categories()

main()
