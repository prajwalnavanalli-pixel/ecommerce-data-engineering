from pymongo import MongoClient

client = MongoClient("mongodb://172.29.176.1:27017/")

db = client["ecommerce_db"]

print("MongoDB connected successfully!")
