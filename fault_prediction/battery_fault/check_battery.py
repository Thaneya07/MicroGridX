# battery_fault/check_battery.py

import pandas as pd

df = pd.read_csv("metadata.csv")

print(df.columns)
print(df.head())
print(df.shape)