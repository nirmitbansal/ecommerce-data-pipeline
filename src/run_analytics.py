# src/run_analytics.py
# Run some example analytic queries on the SQLite database

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "data" / "ecommerce.db"

QUERIES = {
    "total_revenue": """
        SELECT SUM(total_amount) AS total_revenue
        FROM orders;
    """,
    "revenue_by_city": """
        SELECT city, SUM(total_amount) AS revenue
        FROM orders
        GROUP BY city
        ORDER BY revenue DESC;
    """,
    "monthly_revenue": """
        SELECT strftime('%Y-%m', order_date) AS month,
               SUM(total_amount) AS revenue
        FROM orders
        GROUP BY month
        ORDER BY month;
    """
}

def run_queries() -> None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for name, query in QUERIES.items():
        print(f"\n--- {name} ---")
        for row in cursor.execute(query):
            print(row)

    conn.close()

if __name__ == "__main__":
    run_queries()
