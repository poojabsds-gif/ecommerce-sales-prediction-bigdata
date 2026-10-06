import pandas as pd

FILE = "data/cleaned_online_retail.csv"

print("=" * 70)
print("CLEANED DATASET VALIDATION")
print("=" * 70)

df = pd.read_csv(FILE)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nQuantity <= 0:")
print((df["Quantity"] <= 0).sum())

print("\nUnitPrice <= 0:")
print((df["UnitPrice"] <= 0).sum())

print("\nRevenue <= 0:")
print((df["Revenue"] <= 0).sum())

print("\nDate range:")
print(df["InvoiceDate"].min())
print("to")
print(df["InvoiceDate"].max())

print("\nTotal revenue:")
print(df["Revenue"].sum())

print("\nFirst 5 records:")
print(df.head().to_string(index=False))

print("\n" + "=" * 70)
print("VALIDATION COMPLETED")
print("=" * 70)