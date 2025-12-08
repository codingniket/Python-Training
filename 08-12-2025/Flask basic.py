from flask import Flask, request, jsonify

app = Flask(__name__)

items = ["apple","orange","banana","cucumber"]

@app.route("/get-item",methods=["GET"])
def get_item():
    return jsonify(items)

@app.route("/add-item",methods=["POST"])
def add_item():
    data = request.get_json()
    item = data.get("item")
    items.append(item)
    return "Item Added Successfully"


@app.route("/delete-item",methods=["DELETE"])
def delete_by_name():
    data = request.get_json()
    item = data.get("item")
    if item in items:
        items.remove(item)
    return "Deleted Item Successfully"

@app.route("/delete-item2/<int:index>",methods=["DELETE"])
def delete_by_index(index):
    items.pop(index)
    return "Deleted Item Successfully from route2"

@app.route("/update-item/<int:index>",methods=["PUT"])
def put_item(index):
    data = request.get_json()
    new_value = data.get("item")
    items[index] = new_value
    return "Item Updated Successfully"

def page_not_found(e):
    return "Route doesn't exist", 404


if __name__ == "__main__":
    app.run(debug=True)

