import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Models
electrical_model = joblib.load(
    os.path.join(BASE_DIR, "multiclass_xgboost.pkl")
)

battery_model = joblib.load(
    os.path.join(BASE_DIR, "battery_fault", "battery_xgboost.pkl")
)

sensor_model = joblib.load(
    os.path.join(BASE_DIR, "sensor_fault", "sensor_xgboost.pkl")
)

anomaly_model = joblib.load(
    os.path.join(BASE_DIR, "anomaly_detection", "anomaly_xgboost.pkl")
)


def get_fault_predictions(sensor_data):

    # Electrical Fault
    electrical_input = pd.DataFrame([{
        "Ia": sensor_data["Ia"],
        "Ib": sensor_data["Ib"],
        "Ic": sensor_data["Ic"],
        "Va": sensor_data["Va"],
        "Vb": sensor_data["Vb"],
        "Vc": sensor_data["Vc"]
    }])

    electrical_fault = electrical_model.predict(
        electrical_input
    )[0]

    # Battery Health
    battery_input = pd.DataFrame([{
        "ambient_temperature":
        sensor_data["temperature"]
    }])

    battery_health = battery_model.predict(
        battery_input
    )[0]

    # Sensor Fault
    sensor_input = pd.DataFrame([{
        "SensorId": 1,
        "Value": sensor_data["temperature"]
    }])

    sensor_fault = sensor_model.predict(
        sensor_input
    )[0]

    # System Anomaly
    anomaly_input = pd.DataFrame([{
        "AirTemp": sensor_data["temperature"],
        "ProcessTemp": sensor_data["temperature"] + 5,
        "RPM": 1500,
        "Torque": 40,
        "ToolWear": 50
    }])

    anomaly = anomaly_model.predict(
        anomaly_input
    )[0]

    return {
        "electrical_fault": str(electrical_fault),
        "battery_health": round(float(battery_health), 2),
        "sensor_fault": int(sensor_fault),
        "system_anomaly": int(anomaly)
    }