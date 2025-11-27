# SmartPhone ← Camera + Phone
# HybridCar ← ElectricVehicle + FuelVehicle

class Camera :
    def __init__(self,number,power):
        self.number = number
        self.power = power

    def feature(self):
        print(f'You have {self.number} camera each of {self.power} megapixcel')


class Phone:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def details(self):
        print(f"Your phone brand is {self.brand}  and model is {self.model}")

class SmartPhone(Phone,Camera):
    def __init__(self,number,power,brand,model):
        Camera.__init__(self,number,power)
        Phone.__init__(self,brand,model)
    def display(self):
        self.details()
        self.feature()


x = SmartPhone(5,6,"H",21,)
x.display()