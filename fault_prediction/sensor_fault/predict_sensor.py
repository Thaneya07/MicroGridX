import joblib
import pandas as pd

model = joblib.load(
    "sensor_xgboost.pkl"
)

sample = pd.DataFrame([
    {
        "SensorId":1,
        "Value":5
    }
])

pred = model.predict(sample)

if pred[0] == 1:
    print("SENSOR FAILURE ALERT")
else:
    print("SENSOR HEALTHY")