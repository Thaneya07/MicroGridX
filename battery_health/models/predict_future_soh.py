import pandas as pd
import joblib

model = joblib.load(
    "../saved_models/forecast_model.pkl"
)

# Example battery history
history = [
    84,
    83,
    82,
    81,
    80
]

future_predictions = []

for _ in range(20):

    pred = model.predict(
        [history[-5:]]
    )[0]

    # Physics constraint:
    # Battery health cannot improve
    pred = min(
        pred,
        history[-1]- 0.05
    )

    future_predictions.append(pred)

    history.append(pred)

print("\n===== FUTURE SOH =====")

for i, value in enumerate(
    future_predictions,
    start=1
):
    print(
        f"Cycle +{i}: {value:.2f}%"
    )