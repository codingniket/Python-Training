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
df18 = df1.groupby("Region")["Sales"].count()
df19 = df1.groupby("Category")["Profit"].mean()
df20 = df1.groupby("CustomerName")["Sales"].count()
df21 = df1.groupby("SubCategory")["Quantity"].sum()
df22 = df1.groupby("Category")["ShippingDays"].mean()


df23 = pd.pivot_table(
    df1,
    values="Sales",
    index="Region",
    columns="Category",
)

df24 = pd.pivot_table(
    df1,
    values="Profit",
    index="SubCategory",
    columns="Segment",
    fill_value=0,
)
# Pivot showing count of orders by Returned status and Region
df25 = pd.pivot_table(
    df1,
    values="Quantity",
    index="Returned",
    columns="Region",
    aggfunc="count",
    fill_value=0,
)
# Pivot showing average UnitPrice per Category.
df26 = pd.pivot_table(
    df1,
    values="Sales",
    index="UnitPrice",
    columns="Category",
    aggfunc="mean",
    fill_value=0,
)
# Pivot showing total Quantity per Month and Region.
df27 = pd.pivot_table(
    df1,
    values="Quantity",
    index="Region",
    columns=df["OrderDate"].dt.month,
    aggfunc="sum",
    fill_value=0,
)

# Create a discount lookup: Consumer=5, Corporate=8, Home Office=10 and merge it.

discount_lookup = {
    "Consumer": 5,
    "Corporate": 8,
    "Home Office": 10
}
discount_df = pd.DataFrame(list(discount_lookup.items()), columns=["Segment", "DiscountRate"])
df32 = df1.merge(discount_df, on="Segment", how="left")

# Create a region tax table and merge.

tax = {
    "West":5,
    "East":10,
    "South":15,
    "Central":20,
}

tax_df = pd.DataFrame(list(tax.items()), columns=["Region", "Tax"])
df33 = df1.merge(tax_df, on="Region", how="left")
# print(df33)
df33["TaxAmount"] = df33["Profit"] * df33["Tax"] / 100
df331 = df33.groupby("Region")["TaxAmount"].sum()
# print(df331)



# Merge customer-level totals into the main df.
customer_summary = df1.groupby("CustomerID")[["Sales", "Profit"]].sum().reset_index()
print(customer_summary.head())
df1 = df1.merge(customer_summary, on="CustomerID", suffixes=("", "_CustomerTotal"))
# Merge product-level profitability summary
product_summ = df1.groupby("ProductName")[["Sales","Profit"]].sum().reset_index()

df35 = df1.merge(product_summ, on="ProductName", how="left")



# Extract year, month, day from OrderDate

x,y,z = df["OrderDate"].dt.year,df["OrderDate"].dt.month,df["OrderDate"].dt.day

df["DayOfWeek"] = df["OrderDate"].dt.day_name()
# print(df[["OrderDate", "DayOfWeek"]])
df1["ShippingDays"] = (df1["ShipDate"] - df1["OrderDate"]).dt.days
df38 = df1[df1["ShippingDays"] > 5]

df39 = df1.groupby(df["OrderDate"].dt.month_name())["Sales"].sum()

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.plot(df["OrderDate"].dt.month_name(), df["Sales"], marker='o', linestyle='-', color='blue')
# plt.show()



