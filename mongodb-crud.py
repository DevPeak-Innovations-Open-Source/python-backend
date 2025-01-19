import pymongo

class database_manager:
    def __init__(self):
        self.client = None
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = client["productDb"]
            self.collection = self.db["product"]
            print("Connected to MongoDB")
        except:
            print("Error connecting to MongoDB")
    def insert(self, body):
        # Insert data into the database
        try:
            db_id = self.collection.insert_one(body).inserted_id
            print("Data Inserted. ID is:", db_id)
        except:
            print("Error inserting data into the database")
            
    def __del__(self):
        if self.client is not None:
            self.client.close()
            print("Connection Closed")
        

def main():
    db = database_manager()
    product = {
        "name": "Product1",
        "price": 10.99,
    }
    db.insert(product)
    
main()