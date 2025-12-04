import pymysql
import csv

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='company_db'
)

cursor = conn.cursor()

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Employee Salary: "))
    sql = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql, (emp_id, name, salary))
    conn.commit()
    print("Employee added successfully!")

def view_all():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_salary():
    emp_id = int(input("Enter Employee ID to update salary: "))
    new_salary = int(input("Enter new salary: "))
    sql = "UPDATE employees SET salary=%s WHERE id=%s"
    cursor.execute(sql, (new_salary, emp_id))
    conn.commit()
    print("Salary updated successfully!")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete "))
    sql = "DELETE FROM employees WHERE id=%s"
    cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

def search_by_name():
    name = input("Enter Employee Name to search: ")
    sql = "SELECT * FROM employees WHERE name LIKE %s"
    cursor.execute(sql, ("%" + name + "%",))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No employee found with that name.")

def export_to_csv():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    with open("employees.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Salary"])
        writer.writerows(rows)
    print("Data exported to employees.csv")


choice = int(input("Enter the following choices\n 1.Add employee \n2.View all employees\n 3.Update Salary \n4.Delete Employee \n5. Update Salary \n 6. Export CSV \n"))

if choice == 1:
    add_employee()
elif choice == 2:
    view_all()
elif choice == 3:
    update_salary()
elif choice == 4:
    delete_employee()
elif choice == 5:
    search_by_name()
elif choice == 6:
    export_to_csv()
else:
    print("Invalid choice, try again.")
cursor.close()
conn.close()