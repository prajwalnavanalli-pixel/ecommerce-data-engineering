
import pandas as pd
from bson.json_util import loads
from pathlib import Path

# Define folders
raw_folder = Path("data/raw")
processed_folder = Path("data/processed")

# Create processed folder
processed_folder.mkdir(parents=True, exist_ok=True)

# Collections to transform
collections = ["customers", "products", "orders"]

for collection in collections:

    # Read JSON file
    file_path = raw_folder / f"{collection}.json"

    with open(file_path, "r", encoding="utf-8") as file:
        records = loads(file.read())

    # Convert JSON records into DataFrame
    df = pd.DataFrame(records)

    # Remove MongoDB internal ID
    df = df.drop(columns=["_id"], errors="ignore")

    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Fix customer ID mismatch in orders
    if collection == "orders" and "customer_id" in df.columns:
        df["customer_id"] = pd.to_numeric(
            df["customer_id"].astype(str).str.replace(
                r"^C", "", regex=True
            )
        )

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove extra spaces from text columns
    for column in df.select_dtypes(include=["object", "str"]).columns:
        df[column] = df[column].apply(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # Save cleaned data
    output_file = processed_folder / f"{collection}.csv"
    df.to_csv(output_file, index=False)

    print(f"{collection}: {len(df)} records transformed")

print("Data transformation completed!")

