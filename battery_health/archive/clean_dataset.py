import pandas as pd

df = pd.read_csv(
    "../processed_dataset/battery_features_v2.csv"
)

# Convert numeric columns
df["capacity"] = pd.to_numeric(
    df["capacity"],
    errors="coerce"
)

df["Re"] = pd.to_numeric(
    df["Re"],
    errors="coerce"
)

df["Rct"] = pd.to_numeric(
    df["Rct"],
    errors="coerce"
)

# Remove rows with missing SOH
df = df.dropna(subset=["soh"])

# Remove any remaining missing values
df = df.dropna()

df.to_csv(
    "../processed_dataset/battery_features_clean.csv",
    index=False
)

print(df.info())

print(
    "\nRows:",
    len(df)
)

print(
    "\nDataset Cleaned Successfully!"
)