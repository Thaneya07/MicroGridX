import json
from fault_integration import get_fault_predictions

# Sample sensor values
sensor_data = {
    "Ia": 100,
    "Ib": 95,
    "Ic": 98,

    "Va": 0.2,
    "Vb": -0.3,
    "Vc": 0.1,

    "temperature": 32
}

result = get_fault_predictions(
    sensor_data
)

# Simple fault score

fault_score = 0

if result["sensor_fault"] == 1:
    fault_score += 0.3

if result["system_anomaly"] == 1:
    fault_score += 0.4

if result["electrical_fault"] != "0":
    fault_score += 0.3

fault_probability = min(
    round(fault_score, 2),
    1.0
)

if fault_probability < 0.3:
    fault_status = "NORMAL"

elif fault_probability < 0.7:
    fault_status = "WARNING"

else:
    fault_status = "CRITICAL"

output = {

    "fault_probability":
    fault_probability,

    "fault_status":
    fault_status,

    "electrical_fault":
    result["electrical_fault"],

    "battery_health":
    result["battery_health"],

    "sensor_fault":
    result["sensor_fault"],

    "system_anomaly":
    result["system_anomaly"]
}

with open(
    "fault_output.json",
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