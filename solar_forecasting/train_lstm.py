import os
import json
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

# ==========================
# Load JSON Data
# ==========================

with open("data/processed_data.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

print("Dataset Shape:", df.shape)

# ==========================
# Select Features
# ==========================

features = [
    "temperature",
    "humidity",
    "wind-speed",
    "average-wind-speed-(period)",
    "average-pressure-(period)"
]

target = "solar_mw"

# ==========================
# Scale Data
# ==========================

scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

X = scaler_x.fit_transform(df[features])

y = scaler_y.fit_transform(
    df[[target]]
)

# ==========================
# Create Sequences
# ==========================

sequence_length = 24

X_seq = []
y_seq = []

for i in range(sequence_length, len(X)):
    X_seq.append(X[i-sequence_length:i])
    y_seq.append(y[i])

X_seq = np.array(X_seq)
y_seq = np.array(y_seq)

print("X Shape:", X_seq.shape)
print("Y Shape:", y_seq.shape)

# ==========================
# Build LSTM Model
# ==========================

model = Sequential([
    Input(shape=(X_seq.shape[1], X_seq.shape[2])),

    LSTM(64),

    Dense(32, activation="relu"),

    Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

# ==========================
# Train Model
# ==========================

history = model.fit(
    X_seq,
    y_seq,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# ==========================
# Create Models Folder
# ==========================

os.makedirs(
    "models",
    exist_ok=True
)

# ==========================
# Save Model
# ==========================

model.save(
    "models/solar_lstm.keras"
)

print("\nModel Saved Successfully")
print("Location: models/solar_lstm.keras")