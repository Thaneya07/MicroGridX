import pandas as pd

# Load current cleaned dataset
df = pd.read_csv(
    "../processed_dataset/battery_features_clean.csv"
)

print("Original Rows:", len(df))

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

# Remove impossible records
df = df[df["capacity"] > 0]

# Remove missing SOH
df = df.dropna(subset=["soh"])

print("Clean Rows:", len(df))

# Save
df.to_csv(
    "../processed_dataset/battery_features_gold.csv",
    index=False
)

print("Gold Dataset Created Successfully!")