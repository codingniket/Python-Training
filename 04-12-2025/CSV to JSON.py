import json
with open("item.csv","r") as f:
    content = f.readlines()

header = content[0].strip("").split(",")
rows = [line.strip("").split(",") for line in content[1:]]

data = []

for row in rows:
    item = {header[i]: row[i] for i in range(len(header))}
    data.append(item)


with open("products.json", "w") as f:
    json.dump(data, f, indent=4)

print("CSV converted to JSON successfully!")