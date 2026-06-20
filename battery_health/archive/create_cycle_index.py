import pandas as pd

metadata = pd.read_csv(
    "../raw_dataset/cleaned_dataset/metadata.csv"
)

# Sort by battery and test sequence
metadata = metadata.sort_values(
    ["battery_id", "test_id"]
)

metadata["cycle_number"] = (
    metadata.groupby("battery_id")
    .cumcount() + 1
)

metadata.to_csv(
    "../processed_dataset/cycle_mapping.csv",
    index=False
)

print(
    metadata[
        [
            "battery_id",
            "test_id",
            "type",
            "cycle_number"
        ]
    ].head(30)
)

print(
    "\nCycle Mapping Saved!"
)