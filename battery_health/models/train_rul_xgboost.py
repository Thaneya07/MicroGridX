import pandas as pd
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    "../processed_dataset/rul_dataset.csv"
)

print("Dataset Shape:")
print(df.shape)

# ==========================
# Features
# ==========================

X = df[[
    "soh",

    "avg_voltage",
    "max_voltage",
    "min_voltage",

    "avg_current",
    "max_current",

    "avg_temperature",
    "max_temperature",

    "avg_charge_voltage",
    "max_charge_voltage",

    "avg_charge_current",
    "max_charge_current",

    "charge_duration",
    "discharge_duration",

    "Re",
    "Rct",

    "avg_battery_impedance",
    "avg_rectified_impedance"
]]

# Target
y = df["rul"]

# ==========================
# Train/Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ==========================
# Model
# ==========================

model = xgb.XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# ==========================
# Evaluation
# ==========================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

r2 = r2_score(
    y_test,
    y_pred
)

print("\n========== RUL RESULTS ==========")

print(f"MAE  : {mae:.3f}")
print(f"RMSE : {rmse:.3f}")
print(f"R²   : {r2:.4f}")

# ==========================
# Feature Importance
# ==========================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========")

print(importance)

# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    "../saved_models/rul_model.pkl"
)

print(
    "\nRUL Model Saved Successfully!"
)