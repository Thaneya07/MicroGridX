import pandas as pd

df = pd.read_csv("dataset/classData.csv")

df["fault_class"] = (
    df["G"].astype(str)
    + df["C"].astype(str)
    + df["B"].astype(str)
    + df["A"].astype(str)
)

print(
    df["fault_class"]
    .value_counts()
)