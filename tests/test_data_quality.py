
import pandas as pd
from pathlib import Path

DATA_FOLDER = Path("data/processed")


def test_no_missing_values():
    for file in DATA_FOLDER.glob("*.csv"):
        df = pd.read_csv(file)
        assert not df.isnull().any().any(), (
            f"Missing values found in {file.name}"
        )


def test_no_duplicate_records():
    for file in DATA_FOLDER.glob("*.csv"):
        df = pd.read_csv(file)
        assert not df.duplicated().any(), (
            f"Duplicate records found in {file.name}"
        )


def test_customer_ids_match():
    customers = pd.read_csv(DATA_FOLDER / "customers.csv")
    orders = pd.read_csv(DATA_FOLDER / "orders.csv")

    assert orders["customer_id"].isin(
        customers["customer_id"]
    ).all(), "Unmatched customer IDs found"


def test_product_ids_match():
    products = pd.read_csv(DATA_FOLDER / "products.csv")
    orders = pd.read_csv(DATA_FOLDER / "orders.csv")

    assert orders["product_id"].isin(
        products["product_id"]
    ).all(), "Unmatched product IDs found"
