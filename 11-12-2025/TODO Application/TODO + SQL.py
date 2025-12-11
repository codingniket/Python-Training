from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root123',
    database='todo'
)

cursor = conn.cursor()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/",methods=["GET"])
def get_employee():
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/add",methods=["POST"])
def add_item():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")

    if not title:
        return jsonify({"error": "Title Not Provided!"}), 400

    sql = "INSERT INTO tasks (title, description) VALUES (%s, %s)"
    cursor.execute(sql, (title, description))
    conn.commit()
    return "Task added successfully"



@app.route("/del/<int:index>",methods=["DELETE"])
def delete_by_index(index):
    try:
        sql = "DELETE FROM tasks WHERE id=%s"
        cursor.execute(sql, (index,))
        conn.commit()
        return "Task deleted successfully"
    except:
        return jsonify({"error": "Invalid index"}), 400


@app.route("/update/<int:id>",methods=["PUT"])
def put_item(id):
    try:
        data = request.get_json()
        status = data.get("status")

        if not status:
            return jsonify({"error": "Status Required!"}), 400

        sql = "UPDATE tasks SET status=%s WHERE id=%s"
        cursor.execute(sql, (status,id))

        conn.commit()

        return "Records updated successfully"
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def page_not_found(e):
    return "Route doesn't exist", 404


if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
conn.close()