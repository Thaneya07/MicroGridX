import json
import pandas as pd
import joblib

# Load XGBoost model
model = joblib.load("xgboost_fault_model.pkl")

# Read sensor data
with open("sensor_data.json", "r") as f:
    data = json.load(f)

# Convert to dataframe
df = pd.DataFrame({
    "Ia": [data["Ia"]],
    "Ib": [data["Ib"]],
    "Ic": [data["Ic"]],
    "Va": [data["Va"]],
    "Vb": [data["Vb"]],
    "Vc": [data["Vc"]]
})

# Predict
prediction = model.predict(df)

# Output
if prediction[0] == 0:
    print("NORMAL")
else:
    print("FAULT")