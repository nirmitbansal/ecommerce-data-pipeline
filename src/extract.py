# src/extract.py
# Responsible for reading raw data from CSV

import pandas as pd
from pathlib import Path

# Base directory = project root (one level above src/)
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data" / "orders_raw.csv"


def extract_orders() -> pd.DataFrame:
    """Read the raw orders CSV and return a DataFrame."""
    if not RAW_PATH.exists():
        # Helpful error if file is missing
        raise FileNotFoundError(f"Raw file not found: {RAW_PATH}")
    df = pd.read_csv(RAW_PATH)
    return df

if __name__ == "__main__":
    # If you run this file directly, just show first few rows
    df = extract_orders()
    print(df.head())
