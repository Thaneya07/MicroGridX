import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("dataset/detect_dataset.csv")

# Remove unwanted columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df.columns)
print(df['Output (S)'].unique())

X = df[['Ia','Ib','Ic','Va','Vb','Vc']]

y = df['Output (S)']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

joblib.dump(model, "fault_model.pkl")

print("Model Saved!")