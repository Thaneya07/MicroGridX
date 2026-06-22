from flask import Flask, jsonify
from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

@app.route("/api/data")
def data():

    with open(
        os.path.join(
            BASE_DIR,
            "thinking_layer",
            "thinking_output.json"
        )
    ) as f:
        thinking = json.load(f)

    with open(
        os.path.join(
            BASE_DIR,
            "decision_layer",
            "decision_output.json"
        )
    ) as f:
        decision = json.load(f)
    with open(
    os.path.join(
        BASE_DIR,
        "fault_prediction",
        "fault_output.json"
    )
) as f:
     fault = json.load(f)

    return jsonify({

        "energy_status":{

            "solar_power":
            thinking["predicted_solar"],

            "battery_level":
            thinking["battery_soh"],

            "temperature":
            32,

            "fault_probability":
            fault["fault_probability"],

            "predicted_demand":
            thinking["predicted_demand"]
        },

        "decision":{

            "energy_mode":
            "AI_MODE",

            "system_action":
            decision["recommended_action"]
        },

        "system_health":
        thinking["grid_health_score"]

    })
# -------------------------
# Dashboard
# -------------------------

@app.route("/")
def dashboard():

    return send_from_directory(
        os.path.join(
            BASE_DIR,
            "digital-twin"
        ),
        "index.html"
    )


if __name__ == "__main__":
    app.run(debug=True)