n = {
    "name":"Aloo",
    "age":20,
    "salary":1200
}

for key,value in n.items():
    print(key,":",value)

print(n.keys(),n.values())

print(n.get("name"))

n["Nick_Name"] = "Big Aloo"

print(n)

n.pop("Nick_Name")
del n["salary"]
n.clear()

print(n)