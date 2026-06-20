import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

df = pd.read_csv(
    "sensor-fault-detection.csv",
    sep=";"
)

# Create fault labels
df["sensor_fault"] = (
    (df["Value"] < 10) |
    (df["Value"] > 50)
).astype(int)

print("Fault Count:")
print(df["sensor_fault"].value_counts())

X = df[["SensorId", "Value"]]
y = df["sensor_fault"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))

joblib.dump(model, "sensor_xgboost.pkl")

print("\nSensor Model Saved!")