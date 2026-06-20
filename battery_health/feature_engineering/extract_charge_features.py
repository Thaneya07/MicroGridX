import pandas as pd
import os

# Load metadata
metadata = pd.read_csv(
    "../raw_dataset/cleaned_dataset/metadata.csv"
)

# Keep only charge files
charge_files = metadata[
    metadata["type"] == "charge"
]

results = []

for _, row in charge_files.iterrows():

    filename = row["filename"]

    file_path = os.path.join(
        "../raw_dataset/cleaned_dataset/data",
        filename
    )

    try:

        df = pd.read_csv(file_path)

        avg_voltage = df["Voltage_measured"].mean()
        max_voltage = df["Voltage_measured"].max()

        avg_current = df["Current_measured"].mean()
        max_current = df["Current_measured"].max()

        avg_temp = df["Temperature_measured"].mean()
        max_temp = df["Temperature_measured"].max()

        charge_duration = df["Time"].max()

        results.append({

            "battery_id": row["battery_id"],

            "filename": filename,

            "ambient_temperature":
                row["ambient_temperature"],

            "avg_charge_voltage":
                avg_voltage,

            "max_charge_voltage":
                max_voltage,

            "avg_charge_current":
                avg_current,

            "max_charge_current":
                max_current,

            "avg_charge_temperature":
                avg_temp,

            "max_charge_temperature":
                max_temp,

            "charge_duration":
                charge_duration

        })

    except Exception as e:

        print(
            f"Error processing {filename}: {e}"
        )

charge_df = pd.DataFrame(results)

charge_df.to_csv(
    "../processed_dataset/charge_features.csv",
    index=False
)

print(charge_df.head())

print(
    f"\nTotal Records: {len(charge_df)}"
)

print(
    "\nCharge Features Saved Successfully!"
)