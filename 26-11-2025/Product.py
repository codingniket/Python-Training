class Product:
    def __init__(self,name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price * self.quantity

    def display(self):
        print("Product Name:",self.name)
        print("Price per Quantity:",self.price)
        print("Total Quantity:",self.quantity)
        print("Total Cost:",self.calculate())


cal = Product("Amul Milk",180,10)
cal.display()
