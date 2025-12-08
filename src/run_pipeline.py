# src/run_pipeline.py
# Orchestrates the full ETL pipeline: Extract -> Transform -> Load

from extract import extract_orders
from transform import transform_orders, save_clean_data
from load import create_tables, load_orders

def main() -> None:
    print("Step 1: Extract")
    raw_df = extract_orders()

    print("Step 2: Transform")
    clean_df = transform_orders(raw_df)
    save_clean_data(clean_df)

    print("Step 3: Load")
    create_tables()
    load_orders()

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
