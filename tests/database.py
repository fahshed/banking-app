from dotenv import dotenv_values
from pymongo import MongoClient


config = dotenv_values(".env")


async def get_test_collection():
    mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    database = mongodb_client["test-db"]
    collection = database["accounts"]
    print("Connected to the Test Mock MongoDB database!")
    return collection