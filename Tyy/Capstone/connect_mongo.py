from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Mongo URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("✅ Connected successfully to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
