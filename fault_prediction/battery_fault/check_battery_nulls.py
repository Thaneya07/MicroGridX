import pandas as pd

df = pd.read_csv("metadata.csv")

print(df[["type","Capacity","Re","Rct"]].head(20))

print("\nNull Count:\n")
print(df[["Capacity","Re","Rct"]].isnull().sum())