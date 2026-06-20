import pandas as pd
import xgboost as xgb
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv(
    "../processed_dataset/failure_dataset.csv"
)

print("Dataset Shape:")
print(df.shape)

# ==========================
# Features
# ==========================

X = df[[
    "soh",
    "rul",

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
y = df["failure_label"]

# ==========================
# Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==========================
# Model
# ==========================

model = xgb.XGBClassifier(
    n_estimators=300,
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

# ==========================
# Predict
# ==========================

y_pred = model.predict(X_test)

y_prob = model.predict_proba(
    X_test
)[:, 1]

# ==========================
# Metrics
# ==========================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

auc = roc_auc_score(
    y_test,
    y_prob
)

print("\n========== FAILURE MODEL ==========")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"AUC       : {auc:.4f}")

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
# Save
# ==========================

joblib.dump(
    model,
    "../saved_models/failure_model.pkl"
)

print(
    "\nFailure Model Saved!"
)