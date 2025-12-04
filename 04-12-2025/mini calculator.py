class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        try:
            return round(self.a / self.b,2)
        except ZeroDivisionError:
            return "Error division by zero"
    def display(self):
        print("Addition",self.sum())
        print("Multiplication",self.mul())
        print("Division",self.div())
        print("Subtraction",self.sub())

ip = int(input("Enter your number"))
ip2 = int(input("Enter another number"))
x = calculator(ip,ip2)
x.display()
