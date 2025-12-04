class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item, price):
        self.items[item] = price
        print(f"Added {item} for ₹{price}")

    def remove(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item}")
        else:
            print(f"{item} not found in cart")

    def total(self):
        return sum(self.items.values())

    def apply_discount(self, percent):
        discount = (percent / 100) * self.total()
        return self.total() - discount


cart = ShoppingCart()
cart.add("Shoes", 1500)
cart.add("Bag", 1000)
cart.remove("Shoes")

print("Total:", cart.total())
print("Total after 10% discount:", cart.apply_discount(10))