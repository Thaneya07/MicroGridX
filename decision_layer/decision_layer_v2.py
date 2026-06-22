import json
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

with open(
    os.path.join(
        BASE_DIR,
        "thinking_layer",
        "thinking_output.json"
    )
) as f:

    thinking = json.load(f)

grid_health = thinking[
    "grid_health_score"
]

energy_surplus = thinking[
    "energy_surplus"
]

# -------------------------
# Decision Score
# -------------------------

decision_score = round(
    (
        0.6 * grid_health +
        0.4 * min(
            energy_surplus / 1000,
            1
        )
    ),
    3
)

# -------------------------
# Recommended Action
# -------------------------

if decision_score > 0.8:
    action = "Charge Battery"

elif decision_score > 0.5:
    action = "Balanced Operation"

else:
    action = "Energy Saving Mode"

output = {

    "decision_score":
    decision_score,

    "recommended_action":
    action
}

with open(
    "decision_output.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print(
    json.dumps(
        output,
        indent=4
    )
)