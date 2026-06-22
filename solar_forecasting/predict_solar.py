import json
import numpy as np
import pandas as pd

from datetime import datetime
from tensorflow.keras.models import load_model

# ==========================
# Load Trained Model
# ==========================

model = load_model(
    "models/solar_lstm.keras"
)

# ==========================
# Load Dataset
# ==========================

df = pd.read_json(
    "data/processed_data.json"
)

# Find Actual Solar Range
min_solar = df["solar_mw"].min()
max_solar = df["solar_mw"].max()

# ==========================
# Example Input
# ==========================

input_data = np.array([
    [
        [69, 75, 7.5, 8, 29.82]
    ] * 24
])

# ==========================
# Predict
# ==========================

prediction = model.predict(input_data)

scaled_prediction = prediction[0][0]

# Convert Back To Actual MW
actual_prediction = (
    scaled_prediction *
    (max_solar - min_solar)
) + min_solar

# ==========================
# Create JSON Output
# ==========================

output = {
    "timestamp": datetime.now().isoformat(),
    "predicted_solar": round(float(actual_prediction), 2),
    "model": "LSTM"
}

# Save JSON

with open(
    "solar_output.json",
    "w"
) as file:
    json.dump(
        output,
        file,
        indent=4
    )

print("\nSolar Forecast:")
print(json.dumps(output, indent=4))