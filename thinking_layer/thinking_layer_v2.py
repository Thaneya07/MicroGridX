import json

# ==========================
# LOAD AI OUTPUTS
# ==========================

with open(
    "../solar_forecasting/solar_output.json",
    "r"
) as f:
    solar = json.load(f)

with open(
    "../demand_forecasting/prediction_output.json",
    "r"
) as f:
    demand = json.load(f)

with open(
    "../battery_health/battery_intelligence/battery_output.json",
    "r"
) as f:
    battery = json.load(f)

with open(
    "../fault_prediction/final_fault_report.json",
    "r"
) as f:
    fault = json.load(f)

# ==========================
# EXTRACT VALUES
# ==========================

predicted_solar = solar["predicted_solar"]

predicted_demand = demand["predicted_demand"]

battery_soh = battery["soh"]

battery_rul = battery["rul"]

fault_probability = fault["fault_probability"]

# ==========================
# AI FUSION ENGINE
# ==========================

energy_surplus = (
    predicted_solar -
    predicted_demand
)

# Battery Health Score

battery_score = (
    battery_soh / 100
)

# Risk Score

risk_score = (
    1 -
    fault_probability
)

# Grid Stability Score

grid_score = (
    0.4 * battery_score +
    0.3 * risk_score +
    0.3 * (
        predicted_solar /
        max(predicted_demand, 1)
    )
)

# ==========================
# HEALTH LABELS
# ==========================

if grid_score > 0.8:
    grid_status = "STABLE"

elif grid_score > 0.5:
    grid_status = "MODERATE"

else:
    grid_status = "CRITICAL"

# ==========================
# SAVE OUTPUT
# ==========================

output = {

    "predicted_solar":
    predicted_solar,

    "predicted_demand":
    predicted_demand,

    "energy_surplus":
    round(
        energy_surplus,
        2
    ),

    "battery_soh":
    battery_soh,

    "battery_rul":
    battery_rul,

    "fault_probability":
    fault_probability,

    "grid_score":
    round(
        grid_score,
        3
    ),

    "grid_status":
    grid_status
}

with open(
    "thinking_output.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print(
    json.dumps(
        output,
        indent=4
    )
)