import json

with open("product.json", "r") as f:
    products = json.load(f)

discount_rate = 0.10
for i in products:
    original_price = i["price"]
    discounted_price = round(original_price * (1 - discount_rate), 2)
    i["discounted_price"] = discounted_price

with open("product.json", "w") as f:
    json.dump(products, f, indent=4)

print("Discount applied and file updated successfully!")