class Vehicle :
    def __init__(self,fuel,distance):
        self.fuel = fuel
        self.distance = distance

    def max_speed(self):
        print('Max Speed Limit Unknown')



class Car(Vehicle):
    def __init__(self,brand,model,year,fuel,distance):
        super().__init__(fuel,distance)
        self.brand = brand
        self.model = model
        self.year = year
    def max_speed(self):
        print('Max Speed Limit is 200 miles per hour')

class Bike(Vehicle):
    def __init__(self,brand,model,year,fuel,distance):
        super().__init__(fuel,distance)
        self.brand = brand
        self.model = model
        self.year = year

    def max_speed(self):
        print('Max Speed Limit is 80 miles per hour')

x = Car("Mario","XL",2020,5,44)
y = Bike("Yamaha","700",2025,2,100)


x.max_speed()
y.max_speed()
