import pandas as pd 

df = pd.read_csv("customer.csv")

print(df.head())

print("Question 1 \n")

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)

print("\nQuestion 2 \n")

df["Year","Month","Day"] = df["Date"].str.split("-", expand=True)
print(df.head())