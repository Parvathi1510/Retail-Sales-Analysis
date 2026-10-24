from pathlib import Path
import sqlite3
import pandas as pd

data_file = Path("data/cleaned_sales.csv")
database_file = Path("sales.db")

if not data_file.exists():
    raise FileNotFoundError(
        "Cleaned CSV not found. Run clean_data.py first."
    )

df = pd.read_csv(data_file)

# Match the available CSV columns to the database schema
expected_columns = [
    "order_id", "order_date", "ship_date", "ship_mode",
    "customer_id", "customer_name", "segment", "country",
    "city", "state", "postal_code", "region", "product_id",
    "category", "sub_category", "product_name", "sales",
    "quantity", "discount", "profit"
]

for column in expected_columns:
    if column not in df.columns:
        df[column] = None

df = df[expected_columns]

# Store dates as text for simple SQLite queries
for column in ["order_date", "ship_date"]:
    df[column] = df[column].apply(
        lambda value: (
            value.strftime("%Y-%m-%d")
            if pd.notna(value) and hasattr(value, "strftime")
            else (str(value) if pd.notna(value) else None)
        )
    )

with sqlite3.connect(database_file) as connection:
    connection.execute("DROP TABLE IF EXISTS sales")

    connection.execute("""
        CREATE TABLE sales (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,
            order_date TEXT,
            ship_date TEXT,
            ship_mode TEXT,
            customer_id TEXT,
            customer_name TEXT,
            segment TEXT,
            country TEXT,
            city TEXT,
            state TEXT,
            postal_code REAL,
            region TEXT,
            product_id TEXT,
            category TEXT,
            sub_category TEXT,
            product_name TEXT,
            sales REAL,
            quantity INTEGER,
            discount REAL,
            profit REAL
        )
    """)

    df.to_sql(
        "sales",
        connection,
        if_exists="append",
        index=False
    )

    total_rows = connection.execute(
        "SELECT COUNT(*) FROM sales"
    ).fetchone()[0]

print("Database created:", database_file)
print("Rows loaded:", total_rows)
print("Database setup completed successfully!")