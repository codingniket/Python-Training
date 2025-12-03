# import mysql.connector
# connection = mysql.connector.connect(
#     host='localhost',
#     database='world',
#     user='root',
#     password='root123')
# if connection.is_connected():
#     print("Connection Successfully")


import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='retail_db'
)

cursor = conn.cursor()
# Read
cursor.execute("SELECT p.product_name, o.order_date FROM products p INNER JOIN orders o ON o.product_id = p.product_id WHERE p.category = 'Groceries' ORDER BY o.order_date ASC")

#Insert

cursor.execute("""
    INSERT INTO products (product_id, product_name, category, price)
    VALUES (101, 'Milk', 'Groceries', 45.00)
""")

# Update product price
cursor.execute("""
    UPDATE products
    SET price = 50.00
    WHERE product_id = 101
""")
#DELETE
cursor.execute("""
    DELETE FROM products
    WHERE product_id = 101
""")



cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    print(table[0])



conn.commit()
cursor.close()
conn.close()