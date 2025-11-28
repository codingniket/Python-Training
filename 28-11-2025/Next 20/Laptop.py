class Laptop:
    def __init__(self, ram, price, brand):
        self.ram = ram
        self.price = price
        self.brand = brand

    def discount(self,d):
        return self.price - (d * self.price//100)



x = Laptop("32", 100000, "Bapple")
n= int(input("How much discount is needed"))
print(x.discount(n))
