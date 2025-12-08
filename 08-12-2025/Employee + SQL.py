from flask import Flask, request, jsonify
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='employees'
)

cursor = conn.cursor()


app = Flask(__name__)



@app.route("/employee",methods=["GET"])
def get_employee():
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/employee-add",methods=["POST"])
def add_item():
    data = request.get_json()
    empid = data.get("empid")
    name = data.get("name")
    salary = data.get("salary")

    if not empid or not name or not salary:
        return jsonify({"error": "empid, name, and salary are required"}), 400

    sql = "INSERT INTO employee (empid, name, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql, (empid, name, salary))
    conn.commit()
    return "Employee added successfully"



@app.route("/employee-del/<int:index>",methods=["DELETE"])
def delete_by_index(index):
    try:
        sql = "DELETE FROM employee WHERE empid=%s"
        cursor.execute(sql, (index,))
        conn.commit()
        return "Employee deleted successfully"
    except:
        return jsonify({"error": "Invalid index"}), 400


@app.route("/employee-put/<int:empid>",methods=["PUT"])
def put_item(empid):
    try:
        data = request.get_json()
        name = data.get("name")
        salary = data.get("salary")

        if not name or not salary:
            return jsonify({"error": "name, and salary are required"}), 400

        sql = "UPDATE employee SET name=%s, salary=%s WHERE empid=%s"
        cursor.execute(sql, (name, salary, empid))

        conn.commit()

        return "Employee updated successfully"
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def page_not_found(e):
    return "Route doesn't exist", 404


if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
conn.close()