import csv
import json
import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='company_db'
)

cursor = conn.cursor()

def read_csv():
    with open("catelog.csv", "r") as f:
        content = f.readlines()
        for row in content:
            print(row)

def taxes(total,tax,discount):
    new_total = total * (1 - discount / 100)
    new_tax = (tax / 100) * new_total
    final_price = new_total + new_tax
    return final_price


def json_bill(json_file, catalog_file="catelog.csv"):
    # Load catalog
    products = {}
    with open(catalog_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products[int(row["product_id"])] = {
                "name": row["product_name"],
                "price": float(row["price"])
            }


    with open(json_file, "r") as f:
        order = json.load(f)

    total = 0
    print(f"Customer: {order['customer']}")
    print("Items:")

    for item in order["items"]:
        pid = item["product_id"]
        qty = item["quantity"]
        if pid in products:
            pname = products[pid]["name"]
            price = products[pid]["price"]
            subtotal = price * qty
            total += subtotal
            print(f"  {pname} x {qty} = {subtotal}")


    final_price = taxes(total, 5 , 10 ) #Tax followed by discount
    print(f"Total before tax/discount: {total}")
    print(f"Final Price: {final_price}")

    sql = "INSERT INTO mybill (customer_name, total_before, final_price) VALUES (%s, %s, %s)"
    cursor.execute(sql, (order['customer'], total, final_price))
    conn.commit()
    print("Bill stored successfully in database!")


print("\nEnter the following choices:")
print("1. Read Catalog (CSV)")
print("2. Generate Bill from JSON")

choice = int(input("Enter choice: "))

if choice == 1:
    read_csv()
elif choice == 2:
    json_bill("order.json", "catelog.csv")
else:
    print("Invalid choice, try again.")

cursor.close()
conn.close()