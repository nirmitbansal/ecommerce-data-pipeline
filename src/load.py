# src/load.py
# Responsible for loading cleaned data into SQLite

import sqlite3
from pathlib import Path
import pandas as pd

# Base directory = project root (one level above src/)
BASE_DIR = Path(__file__).resolve().parents[1]

DB_PATH = BASE_DIR / "data" / "ecommerce.db"
CLEAN_PATH = BASE_DIR / "data" / "orders_clean.csv"
SQL_PATH = BASE_DIR / "sql" / "create_tables.sql"

def create_tables() -> None:
    """Create the orders table using the SQL script."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SQL_PATH, "r", encoding="utf-8") as f:
        sql_script = f.read()
        cursor.executescript(sql_script)

    conn.commit()
    conn.close()
    print(f"Database and tables ready at {DB_PATH}")

def load_orders() -> None:
    """Load cleaned CSV into the orders table."""
    df = pd.read_csv(CLEAN_PATH)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    print("Loaded cleaned data into 'orders' table")

if __name__ == "__main__":
    create_tables()
    load_orders()
