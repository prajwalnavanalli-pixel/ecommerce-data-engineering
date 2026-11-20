
import pandas as pd
from sqlalchemy import create_engine, URL
from pathlib import Path
from getpass import getpass

# Get PostgreSQL password securely
password = getpass("Enter PostgreSQL password:Prajwal@123 ")

# Connect to PostgreSQL
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="ecommerce_dw"
)

engine = create_engine(connection_url)

try:
    # Read monthly sales report
    df = pd.read_sql(
        "SELECT * FROM monthly_sales_report ORDER BY year, month",
        engine
    )

    # Create output folder
    output_folder = Path("data/output")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Export to CSV
    output_file = output_folder / "monthly_sales_report.csv"
    df.to_csv(output_file, index=False)

    print("Report exported successfully!")
    print("File location:", output_file)
    print(df)

except Exception as error:
    print("Error:", error)

finally:
    engine.dispose()
