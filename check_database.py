import sqlite3

with sqlite3.connect("sales.db") as connection:
    result = connection.execute("""
        SELECT
            COUNT(*) AS total_rows,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(profit), 2) AS total_profit
        FROM sales
    """).fetchone()

print("Total rows:", result[0])
print("Total sales:", result[1])
print("Total profit:", result[2]) 