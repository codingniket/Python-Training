import pymysql
import pandas as pd
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='company_db'
)

cursor = conn.cursor()

def read_orders_from_mysql():
    query = "SELECT * FROM orders"
    order = pd.read_sql(query, conn)
    print("Orders loaded from MySQL")
    return order

def load_products_from_csv():
    product = pd.read_csv("products.csv")
    print("Products loaded from CSV")
    return product

def generate_revenue_dashboard(orders, products):
    merged = pd.merge(orders, products, on="product_id")
    merged["revenue"] = merged["quantity"] * merged["price"]
    dashboard = merged.groupby("product_name")["revenue"].sum().reset_index()
    print("Revenue dashboard generated")
    return dashboard, merged

def compute_top_customers(merged):
    top_customers = merged.groupby("customer_name")["revenue"].sum()
    print("Top 5 customers computed")
    return top_customers[-5]

def save_report_to_excel(dashboard, top_customers):
    with pd.ExcelWriter("final_report.xlsx") as writer:
        dashboard.to_excel(writer, sheet_name="Revenue Dashboard", index=False)
        top_customers.to_excel(writer, sheet_name="Top Customers", index=False)
    print("Final report saved to Excel")

print("\nEnter the following choices:")
print("1. Reads orders from MySQL")
print("2. Loads products from CSV")
print("3. Merges and generates a revenue dashboard")
print("4. Computes top 5 customers")
print("5. Saves final report to Excel")

choice = int(input("Enter choice: "))

orders, products, dashboard, merged, top_customers = None, None, None, None, None

if choice == 1:
    orders = read_orders_from_mysql()
elif choice == 2:
    products = load_products_from_csv()
elif choice == 3:
    if orders is None: orders = read_orders_from_mysql()
    if products is None: products = load_products_from_csv()
    dashboard, merged = generate_revenue_dashboard(orders, products)
elif choice == 4:
    if merged is None:
        if orders is None: orders = read_orders_from_mysql()
        if products is None: products = load_products_from_csv()
        dashboard, merged = generate_revenue_dashboard(orders, products)
    top_customers = compute_top_customers(merged)
elif choice == 5:
    if dashboard is None or top_customers is None:
        if orders is None: orders = read_orders_from_mysql()
        if products is None: products = load_products_from_csv()
        dashboard, merged = generate_revenue_dashboard(orders, products)
        top_customers = compute_top_customers(merged)
    save_report_to_excel(dashboard, top_customers)
else:
    print("Invalid choice, try again.")

cursor.close()
conn.close()
