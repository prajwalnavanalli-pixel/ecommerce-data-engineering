
import subprocess
import sys
import logging
from pathlib import Path

# Create log folder
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_folder / "etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Pipeline stages
scripts = [
    "src/extraction/extract_data.py",
    "src/transformation/transform_data.py",
    "src/validation/validate_data.py"
]

logging.info("ETL Pipeline Started")

# Run extraction, transformation and validation
for script in scripts:
    print(f"\nStarting: {script}")
    logging.info(f"Running: {script}")

    result = subprocess.run(
        [sys.executable, script],
        check=False
    )

    if result.returncode != 0:
        logging.error(f"Pipeline failed at: {script}")
        sys.exit(1)

    logging.info(f"Completed successfully: {script}")

# Run automated tests
print("\nRunning automated tests...")

test_result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/", "-v"],
    check=False
)

if test_result.returncode != 0:
    logging.error("Automated tests failed")
    sys.exit(1)

logging.info("Automated tests passed")

# Load data into PostgreSQL
print("\nStarting PostgreSQL loading...")

load_result = subprocess.run(
    [sys.executable, "src/loading/load_data.py"],
    check=False
)

if load_result.returncode != 0:
    logging.error("PostgreSQL loading failed")
    sys.exit(1)

logging.info("PostgreSQL loading completed successfully")
logging.info("ETL Pipeline Completed Successfully")

print("\nETL PIPELINE COMPLETED SUCCESSFULLY!")


