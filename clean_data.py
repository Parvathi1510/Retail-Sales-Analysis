from pathlib import Path
import pandas as pd
import re

# File locations
input_file = Path("data/sales_data.csv")
output_file = Path("data/cleaned_sales.csv")

# Check whether the dataset exists
if not input_file.exists():
    raise FileNotFoundError(
        "CSV not found. Check data/sales_data.csv"
    )

# Load the original dataset
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# Standardize column names
def clean_column_name(column):
    column = column.strip().lower()
    column = re.sub(r"[^a-z0-9]+", "_", column)
    return column.strip("_")

df.columns = [clean_column_name(col) for col in df.columns]

print("\nCleaned column names:")
print(df.columns.tolist())

# Remove completely duplicated rows
duplicates = df.duplicated().sum()
print("\nDuplicate rows found:", duplicates)

df = df.drop_duplicates()

# Convert date columns when present
for column in ["order_date", "ship_date"]:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column], errors="coerce"
        )

# Convert numeric columns when present
numeric_columns = [
    "sales", "profit", "quantity",
    "discount", "postal_code"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

# Report missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("\nCleaned dataset shape:", df.shape)
print("Cleaned file saved to:", output_file)
print("\nFirst 5 cleaned rows:")
print(df.head())