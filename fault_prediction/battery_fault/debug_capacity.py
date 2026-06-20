import pandas as pd

df = pd.read_csv("metadata.csv")

df = df[df["type"] == "discharge"]

print(df["Capacity"].head(20))

print("\nDatatype:")
print(df["Capacity"].dtype)

print("\nUnique Sample Values:")
print(df["Capacity"].unique()[:20])