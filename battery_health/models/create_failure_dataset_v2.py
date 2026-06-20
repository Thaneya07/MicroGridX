import pandas as pd

df = pd.read_csv(
    "../processed_dataset/battery_features_clean.csv"
)

# Failure Definition
df["failure_label"] = (
    df["soh"] < 70
).astype(int)

print(
    df["failure_label"]
    .value_counts()
)

df.to_csv(
    "../processed_dataset/failure_dataset_v2.csv",
    index=False
)

print("\nFailure Dataset V2 Saved!")