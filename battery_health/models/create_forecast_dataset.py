import pandas as pd

df = pd.read_csv(
    "../processed_dataset/battery_features_gold.csv"
)

df = df.sort_values(
    ["battery_id", "cycle_number"]
)

WINDOW = 5

rows = []

for battery in df["battery_id"].unique():

    battery_df = df[
        df["battery_id"] == battery
    ].sort_values("cycle_number")

    soh_values = battery_df["soh"].values

    if len(soh_values) < WINDOW + 1:
        continue

    for i in range(
        len(soh_values) - WINDOW
    ):

        row = {}

        for j in range(WINDOW):
            row[f"soh_t{j+1}"] = soh_values[i+j]

        row["target_soh"] = soh_values[i+WINDOW]

        rows.append(row)

forecast_df = pd.DataFrame(rows)

print(forecast_df.head())

print("\nRows:", len(forecast_df))

forecast_df.to_csv(
    "../processed_dataset/forecast_dataset.csv",
    index=False
)

print(
    "\nForecast Dataset Created Successfully!"
)