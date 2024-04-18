from dotenv import dotenv_values
from pymongo import MongoClient


config = dotenv_values(".env")


async def get_prod_collection():
    mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    database = mongodb_client[config["DB_NAME"]]
    collection = database["accounts"]
    print("Connected to the MongoDB database!")
    return collection
