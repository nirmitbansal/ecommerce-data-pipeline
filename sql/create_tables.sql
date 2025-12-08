-- sql/create_tables.sql
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    customer_id TEXT,
    order_date TEXT,
    product TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER,
    total_amount REAL,
    city TEXT
);
