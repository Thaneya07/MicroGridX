import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

df = pd.read_csv("dataset/detect_dataset.csv")

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

X = df[['Ia','Ib','Ic','Va','Vb','Vc']]
y = df['Output (S)']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("XGBoost Accuracy:", accuracy)

joblib.dump(model, "xgboost_fault_model.pkl")

print("XGBoost Model Saved!")