import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

# Load Dataset
df = pd.read_csv("dataset/classData.csv")

# Create fault class from G,C,B,A
df["fault_class"] = (
    df["G"].astype(str) +
    df["C"].astype(str) +
    df["B"].astype(str) +
    df["A"].astype(str)
)

# Features
X = df[["Ia", "Ib", "Ic", "Va", "Vb", "Vc"]]

# Labels
y = df["fault_class"]

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print("\nFault Classes:")
print(encoder.classes_)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# XGBoost Model
model = XGBClassifier(
    objective="multi:softmax",
    num_class=len(encoder.classes_),
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)

print("\nTraining XGBoost Model...")
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# Save Model
joblib.dump(model, "multiclass_xgboost.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("\nMulti-Class XGBoost Model Saved!")