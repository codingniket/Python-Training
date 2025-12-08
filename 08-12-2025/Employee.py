from flask import Flask, request, jsonify

app = Flask(__name__)

employee = []

@app.route("/employee",methods=["GET"])
def get_employee():
    return jsonify(employee)

@app.route("/employee-add",methods=["POST"])
def add_item():
    data = request.get_json()
    empid = data.get("empid")
    name = data.get("name")
    salary = data.get("salary")

    if not empid or not name or not salary:
        return jsonify({"error": "empid, name, and salary are required"}), 400

    employee.append({"empid": empid, "name": name, "salary": salary})
    return "Employee added successfully"


@app.route("/employee-del/<int:index>",methods=["DELETE"])
def delete_by_index(index):
    if 0 <= index < len(employee):
        removed = employee.pop(index)
        return jsonify({"message": "Employee deleted successfully", "removed": removed})
    return jsonify({"error": "Invalid index"}), 400


@app.route("/employee-put/<int:index>",methods=["PUT"])
def put_item(index):
    if 0 <= index < len(employee):
        data = request.get_json()
        empid = data.get("empid")
        name = data.get("name")
        salary = data.get("salary")

        if not empid or not name or not salary:
            return jsonify({"error": "empid, name, and salary are required"}), 400

        employee[index] = {"empid": empid, "name": name, "salary": salary}
        return jsonify({"message": "Employee updated successfully"})
    return jsonify({"error": "Invalid index"}), 400


def page_not_found(e):
    return "Route doesn't exist", 404


if __name__ == "__main__":
    app.run(debug=True)

