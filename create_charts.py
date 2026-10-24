import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

with sqlite3.connect("sales.db") as connection:
    # Sales by category
    category_df = pd.read_sql_query("""
        SELECT category, SUM(sales) AS total_sales
        FROM sales
        GROUP BY category
        ORDER BY total_sales DESC
    """, connection)

    # Monthly sales trend
    monthly_df = pd.read_sql_query("""
        SELECT SUBSTR(order_date, 1, 7) AS sales_month,
               SUM(sales) AS total_sales
        FROM sales
        WHERE order_date IS NOT NULL
        GROUP BY sales_month
        ORDER BY sales_month
    """, connection)

# Chart 1: Sales by category
plt.figure(figsize=(8, 5))
plt.bar(category_df["category"], category_df["total_sales"])
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(output_folder / "sales_by_category.png")
plt.close()

# Chart 2: Monthly sales trend
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_df["sales_month"],
    monthly_df["total_sales"],
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "monthly_sales_trend.png")
plt.close()

print("Charts created successfully!")
print("Check the output folder for:")
print("- sales_by_category.png")
print("- monthly_sales_trend.png")