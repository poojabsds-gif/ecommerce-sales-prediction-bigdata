import pandas as pd
from pathlib import Path

# ============================================================
# E-COMMERCE SALES PREDICTION
# Dataset Cleaning and Feature Engineering
# ============================================================

INPUT_FILE = "data/online_retail_II.xlsx"
OUTPUT_FILE = "data/cleaned_online_retail.csv"
REPORT_FILE = "results/data_cleaning_report.txt"


print("=" * 70)
print("E-COMMERCE SALES DATA CLEANING")
print("=" * 70)

# ------------------------------------------------------------
# 1. Read both sheets
# ------------------------------------------------------------

print("\nReading Year 2009-2010...")
df_1 = pd.read_excel(
    INPUT_FILE,
    sheet_name="Year 2009-2010"
)

print("Reading Year 2010-2011...")
df_2 = pd.read_excel(
    INPUT_FILE,
    sheet_name="Year 2010-2011"
)

# ------------------------------------------------------------
# 2. Combine both years
# ------------------------------------------------------------

df = pd.concat([df_1, df_2], ignore_index=True)

original_rows = len(df)

print("\nOriginal records:", original_rows)

# ------------------------------------------------------------
# 3. Standardize column names
# ------------------------------------------------------------

df = df.rename(
    columns={
        "Invoice": "InvoiceNo",
        "StockCode": "StockCode",
        "Description": "Description",
        "Quantity": "Quantity",
        "InvoiceDate": "InvoiceDate",
        "Price": "UnitPrice",
        "Customer ID": "CustomerID",
        "Country": "Country"
    }
)

# ------------------------------------------------------------
# 4. Remove exact duplicate rows
# ------------------------------------------------------------

before = len(df)

df = df.drop_duplicates()

duplicates_removed = before - len(df)

print("Duplicate rows removed:", duplicates_removed)

# ------------------------------------------------------------
# 5. Remove cancelled invoices
# ------------------------------------------------------------

before = len(df)

df["InvoiceNo"] = df["InvoiceNo"].astype(str).str.strip()

df = df[
    ~df["InvoiceNo"].str.upper().str.startswith("C")
]

cancelled_removed = before - len(df)

print("Cancelled invoice rows removed:", cancelled_removed)

# ------------------------------------------------------------
# 6. Remove invalid quantities
# ------------------------------------------------------------

before = len(df)

df = df[df["Quantity"] > 0]

invalid_quantity_removed = before - len(df)

print("Invalid quantity rows removed:", invalid_quantity_removed)

# ------------------------------------------------------------
# 7. Remove invalid prices
# ------------------------------------------------------------

before = len(df)

df = df[df["UnitPrice"] > 0]

invalid_price_removed = before - len(df)

print("Invalid price rows removed:", invalid_price_removed)

# ------------------------------------------------------------
# 8. Remove rows with missing Description
# ------------------------------------------------------------

before = len(df)

df = df.dropna(subset=["Description"])

missing_description_removed = before - len(df)

print("Missing description rows removed:", missing_description_removed)

# ------------------------------------------------------------
# 9. Convert InvoiceDate
# ------------------------------------------------------------

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

before = len(df)

df = df.dropna(subset=["InvoiceDate"])

invalid_date_removed = before - len(df)

print("Invalid date rows removed:", invalid_date_removed)

# ------------------------------------------------------------
# 10. Create Revenue
# ------------------------------------------------------------

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# ------------------------------------------------------------
# 11. Create time features
# ------------------------------------------------------------

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

# ------------------------------------------------------------
# 12. Arrange columns
# ------------------------------------------------------------

columns = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
    "Revenue",
    "Year",
    "Month",
    "Day",
    "DayOfWeek"
]

df = df[columns]

# ------------------------------------------------------------
# 13. Final statistics
# ------------------------------------------------------------

final_rows = len(df)

print("\n" + "=" * 70)
print("FINAL CLEAN DATASET")
print("=" * 70)

print("Original records :", original_rows)
print("Final records    :", final_rows)
print("Records removed  :", original_rows - final_rows)

print("\nColumns:")
print(df.columns.tolist())

print("\nDate range:")
print(df["InvoiceDate"].min())
print("to")
print(df["InvoiceDate"].max())

print("\nTotal revenue:")
print(df["Revenue"].sum())

# ------------------------------------------------------------
# 14. Save cleaned CSV
# ------------------------------------------------------------

Path("data").mkdir(exist_ok=True)
Path("results").mkdir(exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nClean dataset saved to:")
print(OUTPUT_FILE)

# ------------------------------------------------------------
# 15. Create cleaning report
# ------------------------------------------------------------

report = f"""
E-COMMERCE SALES PREDICTION
DATA CLEANING REPORT
==============================

Original records:
{original_rows}

Duplicate rows removed:
{duplicates_removed}

Cancelled invoice rows removed:
{cancelled_removed}

Invalid quantity rows removed:
{invalid_quantity_removed}

Invalid price rows removed:
{invalid_price_removed}

Missing description rows removed:
{missing_description_removed}

Invalid date rows removed:
{invalid_date_removed}

Final records:
{final_rows}

Final columns:
{", ".join(df.columns)}

Date range:
{df["InvoiceDate"].min()} to {df["InvoiceDate"].max()}

Total revenue:
{df["Revenue"].sum():.2f}

Missing Customer IDs were retained because
CustomerID is not mandatory for the primary
sales and demand prediction objective.
"""

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write(report)

print("\nCleaning report saved to:")
print(REPORT_FILE)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)