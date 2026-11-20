
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

try:
    # Test connection
    client.admin.command("ping")
    print("MongoDB connection successful!")

    # Select database
    db = client["ecommerce_db"]

    # Create customers collection
    customers = db["customers"]

    # Customer records
    customer_data = [
        {
            "customer_id": 101,
            "name": "Rahul",
            "email": "rahul@gmail.com",
            "city": "Bangalore",
            "age": 25
        },
        {
            "customer_id": 102,
            "name": "Priya",
            "email": "priya@gmail.com",
            "city": "Mumbai",
            "age": 28
        },
        {
            "customer_id": 103,
            "name": "Amit",
            "email": "amit@gmail.com",
            "city": "Delhi",
            "age": 30
        }
    ]

    # Insert customers
    for customer in customer_data:
        customers.update_one(
            {"customer_id": customer["customer_id"]},
            {"$set": customer},
            upsert=True
        )

    print("Customers inserted successfully!")

    # Display customers
    print("\nCustomer Records:")

    for customer in customers.find({}, {"_id": 0}):
        print(customer)
        
 
    # Create products collection
    products = db["products"]

    # Product data
    product_data = [
        {
            "product_id": "P101",
            "name": "Laptop",
            "category": "Electronics",
            "brand": "Dell",
            "price": 55000,
            "stock": 20
        },
        {
            "product_id": "P102",
            "name": "Smartphone",
            "category": "Electronics",
            "brand": "Samsung",
            "price": 25000,
            "stock": 35
        },
        {
            "product_id": "P103",
            "name": "Headphones",
            "category": "Accessories",
            "brand": "Sony",
            "price": 3000,
            "stock": 50
        }
    ]

    # Insert or update products
    for product in product_data:
        products.update_one(
            {"product_id": product["product_id"]},
            {"$set": product},
            upsert=True
        )

    print("Products inserted successfully!")

    # Display products
    print("\nProduct Records:")

    for product in products.find({}, {"_id": 0}):
        print(product)
       

except Exception as e:
    print("Error:", e)

finally:
    client.close()

