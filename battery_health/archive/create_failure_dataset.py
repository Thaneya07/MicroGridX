import pandas as pd

df = pd.read_csv(
    "../processed_dataset/rul_dataset.csv"
)

# Failure label
df["failure_label"] = (
    df["rul"] <= 30
).astype(int)

print(
    df[
        ["rul", "failure_label"]
    ].head(50)
)

print("\nClass Distribution:")
print(
    df["failure_label"]
    .value_counts()
)

df.to_csv(
    "../processed_dataset/failure_dataset.csv",
    index=False
)

print(
    "\nFailure Dataset Saved!"
)