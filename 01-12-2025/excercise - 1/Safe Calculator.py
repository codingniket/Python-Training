class Calculator:
    def __init__(self,a:int,b:int):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b

    def subtraction(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        try:
            print(self.a / self.b)
        except ZeroDivisionError:
            print("Cannot divide by zero")



    def display(self):
        print("Addition",self.addition())
        print("Substraction",self.subtraction())
        print("Multiplication",self.multiplication())
        self.division()

try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    calculator = Calculator(x, y)
    calculator.display()
except ValueError:
    print("Invalid input")



