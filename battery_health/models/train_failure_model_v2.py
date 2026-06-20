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

# ======================
# Load Dataset
# ======================

df = pd.read_csv(
    "../processed_dataset/failure_dataset_v2.csv"
)

# ======================
# Features
# ======================

X = df[[
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

# ======================
# Split
# ======================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ======================
# Model
# ======================

model = xgb.XGBClassifier(
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

y_pred = model.predict(X_test)

y_prob = model.predict_proba(
    X_test
)[:,1]

# ======================
# Metrics
# ======================

print("\n===== RESULTS =====")

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            y_pred
        ),
        4
    )
)

print(
    "Precision:",
    round(
        precision_score(
            y_test,
            y_pred
        ),
        4
    )
)

print(
    "Recall:",
    round(
        recall_score(
            y_test,
            y_pred
        ),
        4
    )
)

print(
    "F1:",
    round(
        f1_score(
            y_test,
            y_pred
        ),
        4
    )
)

print(
    "AUC:",
    round(
        roc_auc_score(
            y_test,
            y_prob
        ),
        4
    )
)

# ======================
# Feature Importance
# ======================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)

# ======================
# Save
# =====================

joblib.dump(
    model,
    "../saved_models/failure_model_v2.pkl"
)

print(
    "\nFailure Model V2 Saved!"
)