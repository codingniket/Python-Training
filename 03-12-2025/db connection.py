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
    database='company_db'
)

cursor = conn.cursor()

cursor.execute("select * from employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()