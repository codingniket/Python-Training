import pandas as pd
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
combined = pd.merge(customers, orders, on="customer_id")
print("Combined Report:\n", combined.head())