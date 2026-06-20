import pandas as pd

# Load datasets
cycles = pd.read_csv(
    "../processed_dataset/battery_cycles.csv"
)

discharge = pd.read_csv(
    "../processed_dataset/discharge_features.csv"
)

charge = pd.read_csv(
    "../processed_dataset/charge_features.csv"
)

# -------------------------
# Merge discharge features
# -------------------------

battery_features = cycles.merge(
    discharge,
    left_on="discharge_file",
    right_on="filename",
    how="left"
)

# -------------------------
# Merge charge features
# -------------------------

battery_features = battery_features.merge(
    charge,
    left_on="charge_file",
    right_on="filename",
    how="left",
    suffixes=("_discharge", "_charge")
)

# -------------------------
# Calculate SOH
# -------------------------

RATED_CAPACITY = 2.0

battery_features["soh"] = (
    pd.to_numeric(
        battery_features["capacity"],
        errors="coerce"
    ) / RATED_CAPACITY
) * 100

# -------------------------
# Keep important columns
# -------------------------

battery_features = battery_features[[
    "battery_id",
    "cycle_number",

    "capacity",
    "soh",

    "avg_voltage",
    "max_voltage",
    "min_voltage",

    "avg_current",
    "max_current",

    "avg_temperature",
    "max_temperature",

    "avg_charge_voltage",
    "max_charge_voltage",

    "avg_charge_current",
    "max_charge_current",

    "charge_duration",
    "discharge_duration"
]]

# Save
battery_features.to_csv(
    "../processed_dataset/battery_features.csv",
    index=False
)

print(battery_features.head())

print(
    "\nRows:",
    len(battery_features)
)

print(
    "\nBattery Features Dataset Created Successfully!"
)