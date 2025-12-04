import pandas as pd
df = pd.read_csv('retail.csv')
print(df.head())

total_sales = df['Quantity'].sum()
total_revenue = df['Total Amount'].sum()

top_five = df.groupby("Product Category")["Quantity"].sum()

# 1.
print("Total Sales",total_sales)
print("Total Revenue",total_revenue)
print("Top Five\n",top_five[:5])

# 2.
print(df.isnull().sum())
print("Top Five\n",top_five[:5])

# 3.
# Group by product category and calculate: total sales, count of orders, average price.
total_sales = df.groupby("Product Category")["Total Amount"].sum()
total_order = df.groupby("Product Category")["Total Amount"].count()
total_avg = df.groupby("Product Category")["Total Amount"].mean()

print("Total Sales",total_sales)
print("Total Order",total_order)
print("Total Avg",total_avg)

# 4.
df["DiscountedPrice"] = df["Total Amount"] * 0.9
print(df.head())

# 5.
ans = df[df["Total Amount"] > 5000]
print(ans)

# 6.
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
ans = pd.pivot_table(
    df,
    values="Total Amount",
    index="Product Category",
    columns="Month",
    aggfunc='sum',
    fill_value=0
)
print(ans)

7.
Q1 = df['Total Amount'].quantile(0.25)
Q3 = df['Total Amount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_df = df[(df['Total Amount'] >= lower_bound) & (df['Total Amount'] <= upper_bound)]

print("Original dataset size:", len(df))
print("Cleaned dataset size:", len(cleaned_df))
print("Cleaned dataset:\n", cleaned_df.head())