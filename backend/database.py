import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "nyarsapp")
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME", "resolutions")

client: AsyncIOMotorClient | None = None
db = None
resolutions_collection = None


def connect_to_mongo():
    """Öppna anslutning mot MongoDB och sätt global collection."""
    global client, db, resolutions_collection
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[MONGODB_DB_NAME]
    resolutions_collection = db[MONGODB_COLLECTION_NAME]


def close_mongo_connection():
    """Stäng anslutningen när appen slutar."""
    global client
    if client:
        client.close()
