import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

print("Loading dataset...")

# Load dataset
df = pd.read_csv("metadata.csv")

# Keep only discharge cycles
df = df[df["type"] == "discharge"].copy()

# Convert columns to numeric
df["Capacity"] = pd.to_numeric(
    df["Capacity"],
    errors="coerce"
)

df["ambient_temperature"] = pd.to_numeric(
    df["ambient_temperature"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(
    subset=[
        "ambient_temperature",
        "Capacity"
    ]
)

print("\nDataset Info")
print("-" * 40)
print("Rows Available:", len(df))

print("\nSample Data:")
print(df[["ambient_temperature", "Capacity"]].head())

print("\nData Types:")
print(df[["ambient_temperature", "Capacity"]].dtypes)

print("\nMissing Values:")
print(df[["ambient_temperature", "Capacity"]].isnull().sum())

# Features
X = df[
    [
        "ambient_temperature"
    ]
]

# Target
y = df["Capacity"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining XGBoost Model...")

# Model
model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    objective="reg:squarederror",
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, pred)

print("\nResults")
print("-" * 40)
print("MAE:", mae)

# Save model
joblib.dump(
    model,
    "battery_xgboost.pkl"
)

print("\nBattery Model Saved Successfully!")
print("File: battery_xgboost.pkl")