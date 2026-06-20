import pandas as pd

df = pd.read_csv(
    "../processed_dataset/battery_features_clean.csv"
)

# Calculate total cycles per battery
max_cycles = (
    df.groupby("battery_id")["cycle_number"]
      .max()
      .to_dict()
)

# Create RUL
df["rul"] = df.apply(
    lambda row:
    max_cycles[row["battery_id"]]
    - row["cycle_number"],
    axis=1
)

print(
    df[
        ["battery_id",
         "cycle_number",
         "rul"]
    ].head(20)
)

df.to_csv(
    "../processed_dataset/rul_dataset.csv",
    index=False
)

print("\nRUL Dataset Saved!")
print("Rows:", len(df))