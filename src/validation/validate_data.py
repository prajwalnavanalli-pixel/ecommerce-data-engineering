
import pandas as pd
from pathlib import Path

# Define processed data folder
data_folder = Path("data/processed")

# Load CSV files
customers = pd.read_csv(data_folder / "customers.csv")
products = pd.read_csv(data_folder / "products.csv")
orders = pd.read_csv(data_folder / "orders.csv")

print("STARTING DATA QUALITY VALIDATION")

# Check missing values
for name, df in [
    ("Customers", customers),
    ("Products", products),
    ("Orders", orders)
]:
    print(f"\n{name} validation:")
    print("Missing values:")
    print(df.isnull().sum())

    print("Duplicate rows:", df.duplicated().sum())

# Check customer IDs
invalid_customers = orders[
    ~orders["customer_id"].isin(customers["customer_id"])
]

print("\nOrders with unmatched customer IDs:")
print(invalid_customers[["order_id", "customer_id"]])

# Check product IDs
invalid_products = orders[
    ~orders["product_id"].isin(products["product_id"])
]

print("\nOrders with unmatched product IDs:")
print(invalid_products[["order_id", "product_id"]])

print("\nDATA QUALITY VALIDATION COMPLETED!")
