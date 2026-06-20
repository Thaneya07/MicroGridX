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

    if prob > 1:
        prob = 1

    return round(prob, 2)


def efficiency_score(soh):

    return round(soh, 2)


def maintenance_recommendation(soh):

    if soh > 80:
        return "No Action Required"

    elif soh >= 60:
        return "Schedule Inspection"

    else:
        return "Replace Battery"


# -------------------------
# Example Battery
# -------------------------

soh = 84.5
temperature = 32
impedance = 0.22

status = battery_status(soh)

thermal = thermal_risk(
    temperature
)

risk = risk_score(
    soh,
    temperature,
    impedance
)

failure = failure_probability(
    risk
)

efficiency = efficiency_score(
    soh
)

maintenance = maintenance_recommendation(
    soh
)

print("\n========== BATTERY INTELLIGENCE ==========")

print(f"SOH: {soh:.2f}%")

print(f"Battery Status: {status}")

print(f"Risk Score: {risk}")

print(
    f"Failure Probability: {failure}"
)

print(
    f"Thermal Risk: {thermal}"
)

print(
    f"Efficiency Score: {efficiency}"
)

print(
    f"Maintenance Recommendation: {maintenance}"
)