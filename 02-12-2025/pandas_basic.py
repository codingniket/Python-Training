import pandas as pd

# df = pd.DataFrame({
#     "Name":["John","Doe"],
#     "Marks":[90,None],
#     "Age":[22,34]
#
# })
# df.to_json("student.csv",orient="records",indent=4)
# print("JSON file created")
#
# df = pd.read_json('student.csv')
# print(df)
# print("Execution completed!")
#
# print(df.isnull().sum())
#
# df2 = df.copy()
# print(df2.replace("",91).isnull().sum())
# df2 = df2.dropna()
# print(df2)

df = pd.read_csv("student.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"])
print(df.info())
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df)

high_ele = df[(df["Category"] == "Electronics") & (df["TotalPrice"] > 1000)]
print(high_ele)

so = df.sort_values("TotalPrice", ascending=False)

print(so)

cat = df.groupby("Category")["TotalPrice"].sum()
print(cat)

st = df.groupby("Store")["TotalPrice"].mean()
print(st)

ci = df.groupby("City")["OrderID"].count()
print(ci)


customer = pd.DataFrame({
    "CustomerType":["New","Returning"],
    "Discount":[5,10]
})

df = df.merge(customer, on="CustomerType", how="left")

print(df)