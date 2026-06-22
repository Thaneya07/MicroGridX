import json
import os

# ==========================
# PROJECT ROOT
# ==========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# ==========================
# LOAD AI OUTPUTS
# ==========================

with open(
    os.path.join(
        BASE_DIR,
        "battery_health",
        "battery_intelligence",
        "battery_output.json"
    )
) as f:
    battery = json.load(f)

with open(
    os.path.join(
        BASE_DIR,
        "demand_forecasting",
        "prediction_output.json"
    )
) as f:
    demand = json.load(f)

with open(
    os.path.join(
        BASE_DIR,
        "solar_forecasting",
        "solar_output.json"
    )
) as f:
    solar = json.load(f)

with open(
    os.path.join(
        BASE_DIR,
        "fault_prediction",
        "fault_output.json"
    )
) as f:
    fault = json.load(f)

# ==========================
# EXTRACT AI VALUES
# ==========================

soh = battery["soh"]

battery_failure = battery[
    "failure_probability"
]

predicted_demand = demand[
    "predicted_demand"
]

predicted_solar = solar[
    "predicted_solar"
]

fault_probability = fault[
    "fault_probability"
]

# ==========================
# AI FUSION
# ==========================

energy_surplus = (
    predicted_solar -
    predicted_demand
)

battery_score = soh / 100

energy_score = min(
    predicted_solar /
    max(predicted_demand, 1),
    100
) / 100

risk_score = (
    1 -
    (
        battery_failure +
        fault_probability
    ) / 2
)

grid_health_score = round(
    (
        0.4 * battery_score +
        0.3 * energy_score +
        0.3 * risk_score
    ),
    3
)

# ==========================
# OUTPUT
# ==========================

output = {

    "battery_soh":
    soh,

    "predicted_demand":
    predicted_demand,

    "predicted_solar":
    predicted_solar,

    "energy_surplus":
    round(
        energy_surplus,
        2
    ),

    "battery_failure_probability":
    battery_failure,

    "fault_probability":
    fault_probability,

    "grid_health_score":
    grid_health_score
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

print("\n===== THINKING LAYER OUTPUT =====\n")

print(
    json.dumps(
        output,
        indent=4
    )
)