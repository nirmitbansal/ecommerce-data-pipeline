# src/transform.py
# Responsible for cleaning and transforming the data

import pandas as pd
from pathlib import Path

# Base directory = project root (one level above src/)
BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_PATH = BASE_DIR / "data" / "orders_clean.csv"

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the orders data."""
    
    # Remove duplicate rows if any
    df = df.drop_duplicates()

    # Drop rows where critical columns are missing
    df = df.dropna(subset=["order_id", "price", "quantity", "order_date"])

    # Convert order_date to proper datetime
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])

    # Remove rows with zero/negative price or quantity
    df = df[(df["price"] > 0) & (df["quantity"] > 0)]

    # Create a new column: total_amount = price * quantity
    df["total_amount"] = df["price"] * df["quantity"]

    # Standardize category text (if present)
    if "category" in df.columns:
        df["category"] = df["category"].str.strip().str.title()

    return df

def save_clean_data(df: pd.DataFrame) -> None:
    """Save cleaned data to CSV."""
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved cleaned data to {PROCESSED_PATH}")

if __name__ == "__main__":
    raw = pd.read_csv(BASE_DIR / "data" / "orders_raw.csv")
    clean = transform_orders(raw)
    save_clean_data(clean)
