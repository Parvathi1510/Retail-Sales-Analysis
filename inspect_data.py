from pathlib import Path
import pandas as pd

file_path = Path("data/sales_data.csv")

# Check whether the file exists
if not file_path.exists():
    raise FileNotFoundError(
        "Place sales_data.csv inside the data folder."
    )

# Read the CSV file
df = pd.read_csv(file_path)

# Display basic information
print("\nFIRST 5 ROWS")
print(df.head())

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATASET SHAPE")
print(df.shape)

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())