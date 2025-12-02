import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
print(df.info())

df["ShipDate"] = pd.to_datetime(df["ShipDate"],dayfirst=True)
df["OrderDate"] = pd.to_datetime(df["OrderDate"],dayfirst=True)
print(df.info())

df["ShippingDays"] = df["ShipDate"] - df["OrderDate"]

df["ProfitMargin"] = df["Profit"]/df["Sales"]

df["CustomerName"] = df["CustomerName"].str.title()

df = df[df["Sales"] > 0]

df["Discount"] = df["Discount"].apply(lambda x: f"{x:.2%}")

df1= df.copy()
df2 = df1[df1["Region"]=="West"]
df1= df.copy()
df3 = df1[(df1["Category"]=="Technology") & (df1["Sales"] > 400)]

df4 = df1[df1["Returned"] == "Yes"]

df5 = df1[(df1["Category"] == "Furniture") & (df1["ShipDate"] > "2024-01-20")]

df6 = df1[df1["Profit"] < 20]

df7 = df1.sort_values(by="Sales", ascending=False)

df8 = df1.sort_values(by=["Region","City"], ascending=False)

df9 = df1.sort_values(by="ShippingDays", ascending=False)

df10 = df1.sort_values(by="CustomerName", ascending=True)
df11 = df1.sort_values(by="ProfitMargin", ascending=False)

df12 = df1.groupby("Region")["Sales"].sum()
df13 = df1.groupby("Category")["Sales"].mean()
df14 = df1.groupby("CustomerName")["Sales"].count()
df15 = df1.groupby("SubCategory")["Quantity"].sum()
df16 = df1.groupby("Category")["ShippingDays"].mean()
df17 = df1.groupby("Segment")["Sales"].sum()
print(df17)

