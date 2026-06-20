import pandas as pd

# Load datasets
battery = pd.read_csv(
    "../processed_dataset/battery_features.csv"
)

impedance = pd.read_csv(
    "../processed_dataset/impedance_features.csv"
)

result = []

# Process battery by battery
for battery_id in battery["battery_id"].unique():

    battery_df = battery[
        battery["battery_id"] == battery_id
    ].copy()

    imp_df = impedance[
        impedance["battery_id"] == battery_id
    ].copy()

    battery_df = battery_df.reset_index(drop=True)
    imp_df = imp_df.reset_index(drop=True)

    # If impedance records are fewer
    # use forward fill of last available value
    for i in range(len(battery_df)):

        if i < len(imp_df):

            battery_df.loc[i, "Re"] = imp_df.loc[i, "Re"]
            battery_df.loc[i, "Rct"] = imp_df.loc[i, "Rct"]

            battery_df.loc[i,
                "avg_battery_impedance"
            ] = imp_df.loc[i,
                "avg_battery_impedance"
            ]

            battery_df.loc[i,
                "avg_rectified_impedance"
            ] = imp_df.loc[i,
                "avg_rectified_impedance"
            ]

        else:

            battery_df.loc[i, "Re"] = imp_df.iloc[-1]["Re"]

            battery_df.loc[i, "Rct"] = imp_df.iloc[-1]["Rct"]

            battery_df.loc[i,
                "avg_battery_impedance"
            ] = imp_df.iloc[-1][
                "avg_battery_impedance"
            ]

            battery_df.loc[i,
                "avg_rectified_impedance"
            ] = imp_df.iloc[-1][
                "avg_rectified_impedance"
            ]

    result.append(battery_df)

# Combine all batteries
battery_v2 = pd.concat(
    result,
    ignore_index=True
)

# Save
battery_v2.to_csv(
    "../processed_dataset/battery_features_v2.csv",
    index=False
)

print(battery_v2.head())

print(
    "\nRows:",
    len(battery_v2)
)

print(
    "\nColumns:",
    len(battery_v2.columns)
)

print(
    "\nBattery Features V2 Created Successfully!"
)