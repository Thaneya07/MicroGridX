import pandas as pd
import json

# Load Dataset
df = pd.read_csv(
    "data/solarenergy.csv",
    low_memory=False
)

print("Dataset Loaded Successfully")
print(df.columns)

# Convert Datetime
df["Datetime"] = pd.to_datetime(
    df["Datetime"],
    dayfirst=True
)

# Create Features
df["Hour"] = df["Datetime"].dt.hour
df["Month"] = df["Datetime"].dt.month
df["Day"] = df["Datetime"].dt.day

# Remove missing values
df = df.dropna()

# Convert to JSON
records = df.to_dict(orient="records")

with open(
    "data/processed_data.json",
    "w"
) as file:
    json.dump(
        records,
        file,
        indent=4,
        default=str
    )

print("processed_data.json created successfully")
print("Total Records:", len(records))