import pymongo
from pymongo import MongoClient
from Naruto.config.config import MONGO_URI, DB_NAME

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]

# User collection
users_collection = db["users"]

def add_user(user_id, username):
    user_data = {
        "_id": user_id,
        "username": username,
        "money": 100,  # Initial money amount
        # Add more fields as needed for user data
    }
    users_collection.insert_one(user_data)

def get_user(user_id, username):
    return users_collection.find_one({"_id": user_id, "username": username})

def update_money(user_id, amount):
    users_collection.update_one({"_id": user_id}, {"$inc": {"money": amount}})

# Add more database functions as needed

# Load the database
def load_db(app):
    # Perform any necessary database setup or initialization
    # This function could be called in your main __main__.py
    pass
