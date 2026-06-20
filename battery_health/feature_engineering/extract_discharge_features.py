import pandas as pd
import os
print("Script Started")
# Load metadata
metadata = pd.read_csv(
    "../raw_dataset/cleaned_dataset/metadata.csv"
)
print("Metadata Loaded")
print(metadata.head())
# Keep only discharge files
discharge_files = metadata[
    metadata["type"] == "discharge"
]

results = []

for _, row in discharge_files.iterrows():

    filename = row["filename"]

    file_path = os.path.join(
        "../raw_dataset/cleaned_dataset/data",
        filename
    )

    try:

        df = pd.read_csv(file_path)

        avg_voltage = df["Voltage_measured"].mean()
        max_voltage = df["Voltage_measured"].max()
        min_voltage = df["Voltage_measured"].min()

        avg_current = df["Current_measured"].mean()
        max_current = df["Current_measured"].max()

        avg_temp = df["Temperature_measured"].mean()
        max_temp = df["Temperature_measured"].max()

        duration = df["Time"].max()

        results.append({

            "battery_id": row["battery_id"],

            "filename": filename,

            "ambient_temperature":
                row["ambient_temperature"],

            "capacity": row["Capacity"],

            "avg_voltage": avg_voltage,
            "max_voltage": max_voltage,
            "min_voltage": min_voltage,

            "avg_current": avg_current,
            "max_current": max_current,

            "avg_temperature": avg_temp,
            "max_temperature": max_temp,

            "discharge_duration": duration

        })

    except Exception as e:

        print(
            f"Error processing {filename}: {e}"
        )

# Create DataFrame
features_df = pd.DataFrame(results)

# Save
features_df.to_csv(
    "../processed_dataset/discharge_features.csv",
    index=False
)

print(features_df.head())

print(
    f"\nTotal Records: {len(features_df)}"
)

print(
    "\nDischarge Features Saved Successfully!"
)