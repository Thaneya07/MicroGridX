import pandas as pd

metadata = pd.read_csv(
    "../raw_dataset/cleaned_dataset/metadata.csv"
)

results = []

for battery in metadata["battery_id"].unique():

    battery_df = metadata[
        metadata["battery_id"] == battery
    ].sort_values("test_id")

    charges = battery_df[
        battery_df["type"] == "charge"
    ]

    discharges = battery_df[
        battery_df["type"] == "discharge"
    ]

    cycle_count = min(
        len(charges),
        len(discharges)
    )

    for i in range(cycle_count):

        results.append({

            "battery_id": battery,

            "cycle_number": i + 1,

            "charge_file":
                charges.iloc[i]["filename"],

            "discharge_file":
                discharges.iloc[i]["filename"]

        })

cycles = pd.DataFrame(results)

cycles.to_csv(
    "../processed_dataset/battery_cycles.csv",
    index=False
)

print(cycles.head(20))

print(
    f"\nTotal Cycles: {len(cycles)}"
)