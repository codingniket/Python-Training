import pandas as pd

df = pd.read_csv("customer.csv")

print(df.head())

print("Question 1 \n")

print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)

print("\nQuestion 2 \n")

df[["Year","Month","Day"]] = df["Date"].str.split("-", expand=True)
print(df.head())

print("\nQuestion 3 \n")
store = df.groupby("Store")["TotalPrice"].sum()
city = df.groupby("City")["TotalPrice"].sum()
category = df.groupby("Store")["TotalPrice"].sum()
print(store)
print(city)
print(category)

print("\nQuestion 4 \n")
find = df.sort_values(by="TotalPrice",ascending=False)
print(find.head(5))


print("\nQuestion 5 \n")
electronics = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
print(electronics)

print("\nQuestion 6 \n")

df["Discount"] = df.apply(
    lambda row: row["TotalPrice"] * 0.05 if row["CustomerType"] == "New" else row["TotalPrice"] * 0.10,
    axis=1
)

df["Payable"] = df["TotalPrice"] - df["Discount"]

print(df)

print("\nQuestion 7 \n")
mode = df["PaymentMethod"].value_counts()
print(mode)

print("\n Question 8 \n")

qty = df.groupby("Category")["Quantity"].sum()
print(qty)
sales = df.groupby("Category")["TotalPrice"].sum()
print(sales)

print("\nQuestion 9 \n")

sales = df.groupby("Store")["Quantity"].sum().sort_values(ascending=False)
print(sales)
print("\nQuestion 10 \n")

a = df.apply(
    lambda row: row["Product"] if ("a" in row["Product"] or "A" in row["Product"]) else None,
    axis=1
)
print(a)

print("\nQuestion 11 \n")
date = df.sort_values(by=["Date","TotalPrice"], ascending=False)
print(date)

print("\nQuestion 12 \n")
avg = df.groupby("CustomerType")["TotalPrice"].mean()
print(avg)

print("\nQuestion 13 \n")
pivot = pd.pivot_table(
    df,
    values="TotalPrice",
    index="Category",
    columns="PaymentMethod",
    aggfunc="sum",
    dropna=True,
    fill_value=0,
)

print(pivot)


print("\nQuestion 14 \n")

df2 = df[df["Category"] == "Electronics"]

df.to_csv("customer_electronics.csv",index=False)

print("Success")

print("\nQuestion 15 \n")
res =(df.query("Quantity >= 2")
    .query("Category == 'Apparel'")
    .assign(TotalValue=lambda x: x["Quantity"] * x["UnitPrice"])
    .sort_values("TotalValue", ascending=False)
    .reset_index(drop=True)
)
print(res)
