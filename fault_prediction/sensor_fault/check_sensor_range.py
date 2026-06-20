import pandas as pd

df = pd.read_csv(
    "sensor-fault-detection.csv",
    sep=";"
)

print(df["Value"].describe())