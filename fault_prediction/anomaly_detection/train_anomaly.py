import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

print("Loading AI4I Dataset...")

# Load dataset
df = pd.read_csv("ai4i2020.csv")

# Rename columns for XGBoost compatibility
df = df.rename(columns={
    "Air temperature [K]": "AirTemp",
    "Process temperature [K]": "ProcessTemp",
    "Rotational speed [rpm]": "RPM",
    "Torque [Nm]": "Torque",
    "Tool wear [min]": "ToolWear",
    "Machine failure": "MachineFailure"
})

print("\nDataset Shape:")
print(df.shape)

print("\nFailure Distribution:")
print(df["MachineFailure"].value_counts())

# Features
X = df[
    [
        "AirTemp",
        "ProcessTemp",
        "RPM",
        "Torque",
        "ToolWear"
    ]
]

# Target
y = df["MachineFailure"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining XGBoost Model...")

# XGBoost Model
model = XGBClassifier(
    objective="binary:logistic",
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, pred)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, pred))

# Save model
joblib.dump(
    model,
    "anomaly_xgboost.pkl"
)

print("\nAnomaly Detection Model Saved!")
print("Saved File: anomaly_xgboost.pkl")