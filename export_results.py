import sqlite3
from pathlib import Path
import pandas as pd

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

queries = {
    "sales_by_category.csv": """
        SELECT category,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    """,
    "sales_by_region.csv": """
        SELECT region,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        GROUP BY region
        ORDER BY total_sales DESC
    """,
    "top_10_products.csv": """
        SELECT product_name,
               ROUND(SUM(sales), 2) AS total_sales
        FROM sales
        GROUP BY product_name
        ORDER BY total_sales DESC
        LIMIT 10
    """,
    "monthly_sales.csv": """
        SELECT SUBSTR(order_date, 1, 7) AS sales_month,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM sales
        WHERE order_date IS NOT NULL
        GROUP BY sales_month
        ORDER BY sales_month
    """
}

with sqlite3.connect("sales.db") as connection:
    for filename, query in queries.items():
        result = pd.read_sql_query(query, connection)
        result.to_csv(output_folder / filename, index=False)
        print(f"Saved: {filename} ({len(result)} rows)")

print("All analysis results exported successfully!")