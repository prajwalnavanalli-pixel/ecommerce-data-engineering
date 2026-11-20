from pymongo import MongoClient
from bson.json_util import dumps
from pathlib import Path

# Connect to MongoDB
client = MongoClient(
    "mongodb://172.29.176.1:27017/",
    serverSelectionTimeoutMS=5000
)

# Select database
db = client["ecommerce_db"]

# Create output folder
output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

# Collections to extract
collections = ["customers", "products", "orders"]

try:
    # Test MongoDB connection
    client.admin.command("ping")
    print("MongoDB connected successfully!")

    # Extract each collection
    for collection_name in collections:

        # Read data from MongoDB
        records = list(db[collection_name].find())

        # Save records as JSON
        file_path = output_folder / f"{collection_name}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(dumps(records, indent=4))

        print(
            f"{collection_name}: "
            f"{len(records)} records extracted"
        )

    print("Data extraction completed successfully!")

except Exception as error:
    print("Data extraction failed:", error)
    raise

finally:
    client.close()
