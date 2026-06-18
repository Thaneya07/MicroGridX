import pandas as pd
import joblib

# Load model
model = joblib.load("fault_model.pkl")

def predict_fault(Ia, Ib, Ic, Va, Vb, Vc):

    data = pd.DataFrame({
        "Ia": [Ia],
        "Ib": [Ib],
        "Ic": [Ic],
        "Va": [Va],
        "Vb": [Vb],
        "Vc": [Vc]
    })

    prediction = model.predict(data)

    if prediction[0] == 0:
        return "NORMAL"
    else:
        return "FAULT"

result = predict_fault(
    -100,
    20,
    80,
    0.3,
    -0.4,
    0.5
)

print("Status:", result)