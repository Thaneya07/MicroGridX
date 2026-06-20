from fault_prediction.fault_integration import get_fault_predictions

def run_decision_engine():

    import json
    from datetime import datetime
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(BASE_DIR, "data", "sample_data.json")

    with open(input_path, "r") as file:
        data = json.load(file)

    # Extract values
    solar_power = data["energy_status"]["solar_power"]
    battery_level = data["energy_status"]["battery_level"]
    environment_signal = data["energy_status"]["temperature"]
    humidity = data["energy_status"]["humidity"]
    predicted_solar = data["energy_status"]["predicted_solar"]
    predicted_demand = data["energy_status"]["predicted_demand"]

    # ==========================================
    # AI FAULT PREDICTION INTEGRATION
    # ==========================================
    fault_results = get_fault_predictions({

        "Ia": data["energy_status"].get("Ia", 5.2),
        "Ib": data["energy_status"].get("Ib", 5.1),
        "Ic": data["energy_status"].get("Ic", 5.0),

        "Va": data["energy_status"].get("Va", 230),
        "Vb": data["energy_status"].get("Vb", 229),
        "Vc": data["energy_status"].get("Vc", 231),

        "temperature": environment_signal
    })

    # ==========================================
    # SMART ENERGY SCORE
    # ==========================================
    energy_score = round(
        (0.5 * solar_power) +
        (0.3 * battery_level * 10) -
        (0.2 * predicted_demand), 2
    )

    # ==========================================
    # DECISION LOGIC
    # ==========================================
    if energy_score >= 150:

        energy_mode = "NORMAL_MODE"
        system_action = "Supply loads and charge battery"
        battery_action = "Charging"
        non_critical_loads = "ON"
        system_health = "GREEN"

    elif 80 <= energy_score < 150:

        energy_mode = "ECO_MODE"
        system_action = "Reduce non-critical loads"
        battery_action = "Use battery backup"
        non_critical_loads = "OFF"
        system_health = "YELLOW"

    else:

        energy_mode = "EMERGENCY_MODE"
        system_action = "Run critical loads only"
        battery_action = "Battery saving"
        non_critical_loads = "OFF"
        system_health = "RED"

    # ==========================================
    # UPDATE JSON
    # ==========================================
    data["decision"]["energy_mode"] = energy_mode
    data["decision"]["system_action"] = system_action
    data["decision"]["battery_action"] = battery_action

    data["system_health"] = system_health

    data["load_priority"]["critical_loads"] = "ON"
    data["load_priority"]["non_critical_loads"] = non_critical_loads

    data["energy_status"]["energy_score"] = energy_score

    # ==========================================
    # STORE FAULT PREDICTIONS
    # ==========================================
    data["fault_prediction"] = fault_results

    # ==========================================
    # SMART ALERTS
    # ==========================================
    alerts = []

    if fault_results["electrical_fault"] != "0000":
        alerts.append("ELECTRICAL_FAULT")

    if fault_results["battery_health"] < 20:
        alerts.append("BATTERY_FAULT_ALERT")

    if fault_results["sensor_fault"] == 1:
        alerts.append("SENSOR_FAILURE_ALERT")

    if fault_results["system_anomaly"] == 1:
        alerts.append("SYSTEM_ANOMALY_DETECTION")

    data["alerts"] = alerts

    # ==========================================
    # SAVE UPDATED INPUT FILE
    # ==========================================
    with open(input_path, "w") as file:
        json.dump(data, file, indent=4)

    # ==========================================
    # OUTPUT JSON
    # ==========================================
    output = {
        "timestamp": datetime.now().isoformat(),
        "energy_status": data["energy_status"],
        "decision": data["decision"],
        "system_health": data["system_health"],
        "load_priority": data["load_priority"],
        "fault_prediction": data["fault_prediction"],
        "alerts": data["alerts"]
    }

    output_path = os.path.join(
        BASE_DIR,
        "data",
        "decision_output.json"
    )

    with open(output_path, "w") as file:
        json.dump(output, file, indent=4)

    return output