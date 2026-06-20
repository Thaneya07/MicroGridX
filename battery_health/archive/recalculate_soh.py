import pandas as pd

df = pd.read_csv(
    "../processed_dataset/battery_features_v2.csv"
)

# Convert columns to numeric
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

# Remove rows with missing capacity
df = df.dropna(subset=["capacity"])

# First capacity of each battery
initial_capacity = (
    df.groupby("battery_id")["capacity"]
      .transform("first")
)

# Correct SOH
df["soh"] = (
    df["capacity"] /
    initial_capacity
) * 100

print("\nSOH Statistics")
print(df["soh"].describe())

print("\nSOH > 100 Count:")
print((df["soh"] > 100).sum())

print("\nTop SOH Values:")
print(
    df[
        ["battery_id","cycle_number","soh"]
    ]
    .sort_values(
        "soh",
        ascending=False
    )
    .head(20)
)

df.to_csv(
    "../processed_dataset/battery_features_clean_v2.csv",
    index=False
)

print("\nDataset Saved Successfully!")