import pandas as pd

df = pd.read_csv("dataset/classData.csv")

print(df[["G", "C", "B", "A"]].head(30))