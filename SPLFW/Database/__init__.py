from config import MONGO_DB_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(MONGO_DB_URL)

db = mongo.SPLFW
