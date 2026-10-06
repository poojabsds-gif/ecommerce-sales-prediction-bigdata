import pandas as pd

FILE = "data/online_retail_II.xlsx"

print("=" * 70)
print("E-COMMERCE ONLINE RETAIL II - DATA QUALITY ANALYSIS")
print("=" * 70)

# ---------------------------------------------------------
# 1. Read both sheets
# ---------------------------------------------------------

print("\nReading Year 2009-2010...")
df1 = pd.read_excel(
    FILE,
    sheet_name="Year 2009-2010"
)

print("Reading Year 2010-2011...")
df2 = pd.read_excel(
    FILE,
    sheet_name="Year 2010-2011"
)

# ---------------------------------------------------------
# 2. Combine both years
# ---------------------------------------------------------

df = pd.concat([df1, df2], ignore_index=True)

print("\n" + "=" * 70)
print("BASIC DATASET INFORMATION")
print("=" * 70)

print("Year 2009-2010 records :", len(df1))
print("Year 2010-2011 records :", len(df2))
print("Combined records       :", len(df))
print("Number of columns      :", len(df.columns))

print("\nColumns:")
for column in df.columns:
    print(" -", column)

# ---------------------------------------------------------
# 3. Data types
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)

# ---------------------------------------------------------
# 4. Missing values
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing = df.isnull().sum()

for column, count in missing.items():
    percentage = (count / len(df)) * 100
    print(f"{column:15} : {count:10} ({percentage:.2f}%)")

# ---------------------------------------------------------
# 5. Duplicate rows
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)

# ---------------------------------------------------------
# 6. Cancelled invoices
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("CANCELLED INVOICES")
print("=" * 70)

invoice_text = df["Invoice"].astype(str)

cancelled = invoice_text.str.startswith("C")

print("Cancelled transaction rows:", cancelled.sum())

# ---------------------------------------------------------
# 7. Quantity analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("QUANTITY ANALYSIS")
print("=" * 70)

print("Minimum quantity:", df["Quantity"].min())
print("Maximum quantity:", df["Quantity"].max())

negative_quantity = (df["Quantity"] < 0).sum()
zero_quantity = (df["Quantity"] == 0).sum()

print("Negative quantity rows:", negative_quantity)
print("Zero quantity rows    :", zero_quantity)

# ---------------------------------------------------------
# 8. Price analysis
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("PRICE ANALYSIS")
print("=" * 70)

print("Minimum price:", df["Price"].min())
print("Maximum price:", df["Price"].max())

zero_price = (df["Price"] == 0).sum()
negative_price = (df["Price"] < 0).sum()

print("Zero price rows    :", zero_price)
print("Negative price rows:", negative_price)

# ---------------------------------------------------------
# 9. Date range
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("DATE RANGE")
print("=" * 70)

dates = pd.to_datetime(df["InvoiceDate"], errors="coerce")

print("Earliest transaction:", dates.min())
print("Latest transaction  :", dates.max())

# ---------------------------------------------------------
# 10. Unique values
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("UNIQUE VALUES")
print("=" * 70)

print("Unique invoices :", df["Invoice"].nunique())
print("Unique products :", df["StockCode"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print("Unique countries:", df["Country"].nunique())

# ---------------------------------------------------------
# 11. Revenue calculation
# ---------------------------------------------------------

df["Revenue"] = df["Quantity"] * df["Price"]

print("\n" + "=" * 70)
print("REVENUE")
print("=" * 70)

print("Total raw revenue:", df["Revenue"].sum())

# ---------------------------------------------------------
# 12. Country distribution
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 COUNTRIES BY TRANSACTION COUNT")
print("=" * 70)

print(df["Country"].value_counts().head(10))

# ---------------------------------------------------------
# 13. Summary
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("DATA QUALITY ANALYSIS COMPLETED")
print("=" * 70)