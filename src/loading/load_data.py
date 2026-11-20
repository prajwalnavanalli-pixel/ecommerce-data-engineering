
import pandas as pd
import os
from sqlalchemy import create_engine, URL
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# PostgreSQL connection
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 5432)),
    database=os.getenv("DB_NAME")
)

engine = create_engine(connection_url)

# CSV folder
folder = Path("data/processed")

# Tables to load
tables = ["customers", "products", "orders"]

try:
    # Test database connection
    with engine.connect() as connection:
        print("PostgreSQL connected successfully!")

    # Load CSV files into PostgreSQL
    for table in tables:
        file_path = folder / f"{table}.csv"

        df = pd.read_csv(file_path)

        df.to_sql(
            table,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table}: {len(df)} records loaded")

    print("All data loaded successfully!")

except Exception as error:
    print("Data loading failed:", error)
    raise

finally:
    engine.dispose()


