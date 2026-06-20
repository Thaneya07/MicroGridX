from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("fault_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    Ia = data["Ia"]
    Ib = data["Ib"]
    Ic = data["Ic"]
    Va = data["Va"]
    Vb = data["Vb"]
    Vc = data["Vc"]

    df = pd.DataFrame({
        "Ia":[Ia],
        "Ib":[Ib],
        "Ic":[Ic],
        "Va":[Va],
        "Vb":[Vb],
        "Vc":[Vc]
    })

    prediction = model.predict(df)

    status = "FAULT" if prediction[0] == 1 else "NORMAL"

    return jsonify({
        "fault_status": status
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)