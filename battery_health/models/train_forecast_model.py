import pandas as pd
import xgboost as xgb
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ======================
# Load Dataset
# ======================

df = pd.read_csv(
    "../processed_dataset/forecast_dataset.csv"
)

print("Dataset Shape:")
print(df.shape)

# ======================
# Features
# ======================

X = df[
    [
        "soh_t1",
        "soh_t2",
        "soh_t3",
        "soh_t4",
        "soh_t5"
    ]
]

y = df["target_soh"]

# ======================
# Split
# ======================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ======================
# Model
# ======================

model = xgb.XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# ======================
# Predict
# ======================

pred = model.predict(X_test)

# ======================
# Metrics
# ======================

mae = mean_absolute_error(
    y_test,
    pred
)

rmse = mean_squared_error(
    y_test,
    pred
) ** 0.5

r2 = r2_score(
    y_test,
    pred
)

print("\n===== FORECAST RESULTS =====")

print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

# ======================
# Save
# ======================

joblib.dump(
    model,
    "../saved_models/forecast_model.pkl"
)

print(
    "\nForecast Model Saved!"
)