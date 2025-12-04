import pymysql
import datetime

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='company_db'
)

cursor = conn.cursor()

def search():
    ip = input("Enter book name or author: ")
    query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(query, ('%' + ip + '%', '%' + ip + '%'))
    results = cursor.fetchall()
    for row in results:
        print(f"BookID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Available: {row[3]}")

def borrow():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    borrow_date = datetime.date.today()
    cursor.execute("INSERT INTO borrow (book_id, member_id, borrow_date) VALUES (%s, %s, %s)",
                   (book_id, member_id, borrow_date))
    cursor.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
    conn.commit()
    print("Book borrowed successfully!")

def rent():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    return_date = datetime.date.today()
    cursor.execute("UPDATE borrow SET return_date = %s WHERE book_id = %s AND member_id = %s AND return_date IS NULL",
                   (return_date, book_id, member_id))
    cursor.execute("UPDATE books SET available = TRUE WHERE book_id = %s", (book_id,))
    conn.commit()
    print("Book returned successfully!")


print("\nEnter the following choices:")
print("1. name/author search")
print("2. To borrow")
print("3. To return")
choice = int(input("Enter choice: "))

if choice == 1:
    search()
elif choice == 2:
    borrow()
elif choice == 3:
    rent()
else:
    print("Invalid choice, try again.")

cursor.close()
conn.close()