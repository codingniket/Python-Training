class Vehicle :
    def __init__(self,fuel,distance):
        self.fuel = fuel
        self.distance = distance

    def sound(self):
        print('Vehicle Sound Boom Boom')

    def milage(self,fuel,distance):
        a=distance//fuel
        print(f"Your Vehicle provide mileage of {a} miles:",)


class Car(Vehicle):
    def __init__(self,brand,model,year,fuel,distance):
        super().__init__(fuel,distance)
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f"Car Details : {self.brand} {self.model} {self.year}")
        self.milage(self.fuel,self.distance)
        self.sound()

class Bike(Vehicle):
    def __init__(self,brand,model,year,fuel,distance):
        super().__init__(fuel,distance)
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f"Car Details : {self.brand} {self.model} {self.year}")
        self.milage(self.fuel,self.distance)
        self.sound()

class Truck(Vehicle):
    def __init__(self,brand,model,year,fuel,distance):
        super().__init__(fuel,distance)
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(f"Car Details : {self.brand} {self.model} {self.year}")
        self.milage(self.fuel,self.distance)
        self.sound()


x = Car("Mario","XL",2020,5,44)
y = Bike("Yamaha","700",2025,2,100)
z = Truck("Ford","Pickup",2022,50,5000)

x.display()
y.display()
z.display()