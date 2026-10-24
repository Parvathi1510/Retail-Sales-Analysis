import sqlite3
from pathlib import Path

query_file = Path("sql/analysis_queries.sql")

if not query_file.exists():
    raise FileNotFoundError(
        "Create sql/analysis_queries.sql first."
    )

sql_text = query_file.read_text(encoding="utf-8")

with sqlite3.connect("sales.db") as connection:
    queries = [
        query.strip()
        for query in sql_text.split(";")
        if query.strip()
    ]

    for number, query in enumerate(queries, start=1):
        print(f"\n{'=' * 50}")
        print(f"QUERY {number}")
        print("=" * 50)

        cursor = connection.execute(query)
        rows = cursor.fetchall()

        if cursor.description:
            columns = [
                item[0] for item in cursor.description
            ]
            print(" | ".join(columns))

            for row in rows:
                print(" | ".join(str(value) for value in row))

print("\nAll SQL queries executed successfully!")