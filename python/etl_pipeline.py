import pandas as pd
from sqlalchemy import create_engine
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Database configuration
DB_URL = "postgresql://sales_admin:admin123@localhost/sales_db"

def load_csv_to_df(filepath):
    """Loads CSV and performs basic cleaning."""
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return None

    df = pd.read_csv(filepath)
    # Basic cleaning: remove duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    if len(df) < initial_count:
        logger.warning(f"Removed {initial_count - len(df)} duplicates from {filepath}")

    return df

def etl_process():
    try:
        engine = create_engine(DB_URL)
        logger.info("Connected to PostgreSQL successfully.")

        # Load order matters because of foreign keys
        tables = [
            ('dim_regions', 'data/raw/dim_regions.csv'),
            ('dim_customers', 'data/raw/dim_customers.csv'),
            ('dim_products', 'data/raw/dim_products.csv'),
            ('dim_sales_reps', 'data/raw/dim_sales_reps.csv'),
            ('fact_sales', 'data/raw/fact_sales.csv')
        ]

        for table_name, file_path in tables:
            logger.info(f"Processing {table_name}...")
            df = load_csv_to_df(file_path)
            if df is not None:
                # Validate data (example: ensure no nulls in PKs)
                if df.iloc[:, 0].isnull().any():
                     logger.error(f"Null values found in primary key column of {table_name}")
                     continue

                # Load into SQL
                df.to_sql(table_name, engine, if_exists='append', index=False)
                logger.info(f"Loaded {len(df)} rows into {table_name}.")
            else:
                logger.error(f"Failed to load data for {table_name}")

        logger.info("ETL Pipeline completed successfully.")

    except Exception as e:
        logger.error(f"ETL Pipeline failed: {e}")

if __name__ == "__main__":
    etl_process()
