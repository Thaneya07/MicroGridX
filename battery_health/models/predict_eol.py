import pandas as pd
import joblib

# =====================
# SETTINGS
# =====================

BATTERY_ID = "B0036"

# =====================
# LOAD DATA
# =====================

df = pd.read_csv(
    "../processed_dataset/battery_features_gold.csv"
)

model = joblib.load(
    "../saved_models/forecast_model.pkl"
)

# =====================
# GET BATTERY HISTORY
# =====================

battery_df = df[
    df["battery_id"] == BATTERY_ID
].sort_values("cycle_number")

# Latest 5 SOH values
history = (
    battery_df["soh"]
    .tail(5)
    .tolist()
)

current_cycle = int(
    battery_df["cycle_number"].max()
)

current_soh = history[-1]

print("\nLatest SOH History:")
print(history)

# =====================
# FORECAST UNTIL EOL
# =====================

forecast_cycles = 0

while history[-1] > 70:

    pred = model.predict(
        [history[-5:]]
    )[0]

    # Physics Constraint
    pred = min(
        pred,
        history[-1] - 0.05
    )

    history.append(pred)

    forecast_cycles += 1

    # Safety Stop
    if forecast_cycles > 500:
        break

# =====================
# RESULTS
# =====================

eol_cycle = current_cycle + forecast_cycles

print("\n========== REAL BATTERY EOL ==========")

print(
    f"Battery ID: {BATTERY_ID}"
)

print(
    f"Current Cycle: {current_cycle}"
)

print(
    f"Current SOH: {current_soh:.2f}%"
)

print(
    f"Predicted EOL Cycle: {eol_cycle}"
)

print(
    f"Remaining Cycles: {forecast_cycles}"
)

print(
    f"Predicted EOL SOH: {history[-1]:.2f}%"
)