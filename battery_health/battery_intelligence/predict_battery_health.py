import pandas as pd
import joblib

# ==========================
# Battery Intelligence Logic
# ==========================

def battery_status(soh):
    if soh > 80:
        return "HEALTHY"
    elif soh >= 60:
        return "WARNING"
    else:
        return "CRITICAL"


def thermal_risk(temp):
    if temp < 35:
        return "LOW"
    elif temp <= 45:
        return "MEDIUM"
    else:
        return "HIGH"


def risk_score(soh, temp, impedance):

    score = 100 - soh

    if temp > 45:
        score += 20

    elif temp > 35:
        score += 10

    if impedance > 0.25:
        score += 10

    return round(score, 2)


def failure_probability(risk):
    prob = risk / 100
    return round(min(prob, 1), 2)


def maintenance_recommendation(soh):

    if soh > 80:
        return "No Action Required"

    elif soh >= 60:
        return "Schedule Inspection"

    else:
        return "Replace Battery"


# ==========================
# Load Model
# ==========================

model = joblib.load(
    "../saved_models/soh_model.pkl"
)

# ==========================
# Sample Battery Features
# ==========================

sample = pd.DataFrame([{
    "avg_voltage": 3.475266,
    "max_voltage": 4.246764,
    "min_voltage": 2.470612,

    "avg_current": -0.952767,
    "max_current": 0.000252,

    "avg_temperature": 8.272423,
    "max_temperature": 12.376816,

    "avg_charge_voltage": 4.193521,
    "max_charge_voltage": 4.214595,

    "avg_charge_current": 0.520792,
    "max_charge_current": 1.494314,

    "charge_duration": 10803.313,
    "discharge_duration": 6436.141,

    "Re": 0.056058,
    "Rct": 0.200970,

    "avg_battery_impedance": 0.213929,
    "avg_rectified_impedance": 0.084121
}])

# ==========================
# Predict SOH
# ==========================

predicted_soh = float(
    model.predict(sample)[0]
)

# ==========================
# Intelligence Layer
# ==========================

temperature = sample["max_temperature"].iloc[0]
impedance = sample["avg_battery_impedance"].iloc[0]

status = battery_status(predicted_soh)

thermal = thermal_risk(temperature)

risk = risk_score(
    predicted_soh,
    temperature,
    impedance
)

failure = failure_probability(risk)

maintenance = maintenance_recommendation(
    predicted_soh
)

# ==========================
# Output
# ==========================

print("\n========== BATTERY REPORT ==========")

print(f"Predicted SOH: {predicted_soh:.2f}%")

print(f"Battery Status: {status}")

print(f"Risk Score: {risk}")

print(f"Failure Probability: {failure}")

print(f"Thermal Risk: {thermal}")

print(f"Efficiency Score: {predicted_soh:.2f}")

print(
    f"Maintenance Recommendation: {maintenance}"
)