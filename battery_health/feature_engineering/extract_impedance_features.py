import pandas as pd
import os
import numpy as np

# Load metadata
metadata = pd.read_csv(
    "../raw_dataset/cleaned_dataset/metadata.csv"
)

# Keep only impedance files
impedance_files = metadata[
    metadata["type"] == "impedance"
]

results = []

for _, row in impedance_files.iterrows():

    filename = row["filename"]

    file_path = os.path.join(
        "../raw_dataset/cleaned_dataset/data",
        filename
    )

    try:

        df = pd.read_csv(file_path)

        # Convert string → complex
        battery_impedance = (
            df["Battery_impedance"]
            .apply(complex)
        )

        rectified_impedance = (
            df["Rectified_Impedance"]
            .apply(complex)
        )

        # Magnitudes
        battery_mag = np.abs(
            battery_impedance
        )

        rectified_mag = np.abs(
            rectified_impedance
        )

        results.append({

            "battery_id":
                row["battery_id"],

            "filename":
                filename,

            "ambient_temperature":
                row["ambient_temperature"],

            "Re":
                row["Re"],

            "Rct":
                row["Rct"],

            "avg_battery_impedance":
                battery_mag.mean(),

            "max_battery_impedance":
                battery_mag.max(),

            "avg_rectified_impedance":
                rectified_mag.mean(),

            "max_rectified_impedance":
                rectified_mag.max()

        })

    except Exception as e:

        print(
            f"Error processing {filename}: {e}"
        )

impedance_df = pd.DataFrame(results)

impedance_df.to_csv(
    "../processed_dataset/impedance_features.csv",
    index=False
)

print(
    impedance_df.head()
)

print(
    f"\nTotal Records: {len(impedance_df)}"
)

print(
    "\nImpedance Features Saved Successfully!"
)