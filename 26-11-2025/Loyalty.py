class Customer:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def check(self):
        if self.age < 25:
            print("You are not eligible for loyalty program.")
        else:
            print("You are eligible for loyalty program.")

cal = Customer("Amul Milk", 32, 'Kashmir')
cal.check()
