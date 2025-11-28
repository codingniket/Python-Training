class Mobile:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"My mobile brand is {self.brand} and model number {self.model} of my phone")

x = Mobile("Bob","cv")
x.display()