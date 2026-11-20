# Enterprise E-commerce Data Engineering Platform

## Project Overview

An end-to-end E-commerce Data Engineering project that extracts data from MongoDB, transforms and cleans it using Python and Pandas, validates data quality, and loads it into a PostgreSQL data warehouse.

Apache Airflow orchestrates the ETL pipeline and automates execution.

## Architecture

```text
MongoDB
   |
   v
Data Extraction (Python)
   |
   v
Raw JSON Files
   |
   v
Data Transformation (Pandas)
   |
   v
Processed CSV Files
   |
   v
Data Quality Validation
   |
   v
Automated Testing (Pytest)
   |
   v
PostgreSQL Data Warehouse
   |
   v
Reporting and Analytics

Apache Airflow: Pipeline Orchestration
```

## Technologies Used

- Python
- MongoDB
- PostgreSQL
- Pandas
- SQLAlchemy
- Apache Airflow
- Pytest
- Git and GitHub

## Project Features

### 1. Data Extraction
- Extracts customers, products and orders from MongoDB.
- Stores extracted records as JSON files.

### 2. Data Transformation
- Converts JSON records into Pandas DataFrames.
- Removes MongoDB internal IDs.
- Standardizes column names.
- Removes duplicate records.
- Cleans unnecessary spaces.
- Standardizes customer IDs.

### 3. Data Quality Validation
- Checks missing values.
- Detects duplicate records.
- Validates customer IDs.
- Validates product IDs.

### 4. Automated Testing
- Tests missing values.
- Tests duplicate records.
- Checks customer ID relationships.
- Checks product ID relationships.

### 5. Data Loading
- Loads processed CSV data into PostgreSQL.
- Uses SQLAlchemy for database connectivity.

### 6. Workflow Orchestration
- Uses Apache Airflow to schedule and execute the ETL pipeline.
- Monitors task execution through the Airflow interface.
- Supports automatic task retries.

## Project Structure

```text
ecommerce-data-engineering/
|
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
|
├── src/
│   ├── extraction/
│   │   └── extract_data.py
│   ├── transformation/
│   │   └── transform_data.py
│   ├── validation/
│   │   └── validate_data.py
│   └── loading/
│       └── load_data.py
|
├── tests/
│   └── test_data_quality.py
|
├── sql/
├── notebooks/
├── config/
├── logs/
|
├── run_pipeline.py
├── export_report.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-data-engineering
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv-wsl
source .venv-wsl/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file with your own PostgreSQL connection settings:

```text
DB_HOST=YOUR_DATABASE_HOST
DB_PORT=5432
DB_NAME=YOUR_DATABASE_NAME
DB_USER=YOUR_DATABASE_USER
DB_PASSWORD=YOUR_DATABASE_PASSWORD
```

Never commit your `.env` file or database credentials to GitHub.

### 5. Run the ETL pipeline

```bash
python run_pipeline.py
```

### 6. Run automated tests

```bash
python -m pytest tests/ -v
```

### 7. Start Airflow

Configure Apache Airflow separately and place the DAG file in its configured DAG folder.

## Current Project Status

- MongoDB extraction: Implemented
- Data transformation: Implemented
- Data quality validation: Implemented
- Automated testing: Implemented
- PostgreSQL loading: Implemented
- Airflow orchestration: Implemented
- Reporting and analytics: Implemented

## Learning Outcomes

This project demonstrates practical experience with:

- ETL pipeline development
- NoSQL and relational databases
- Data cleaning and transformation
- Data quality engineering
- Automated testing
- Data warehouse concepts
- Workflow orchestration
- Python project organization

## Author

Data Engineering Portfolio Project
