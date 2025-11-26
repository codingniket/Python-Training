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
        if self.b == 0:
            return "Division by zero not possible"

        return self.a/self.b

    def display(self):
        print("Addition",self.addition())
        print("Substraction",self.subtraction())
        print("Multiplication",self.multiplication())
        print("Division",self.division())

x = int(input("Enter a number:"))
y = int(input("Enter another number:"))

calculator = Calculator(x,y)
calculator.display()
