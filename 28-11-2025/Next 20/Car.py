class Vehicle :
    def __init__(self,fuel,distance):
        self.fuel = fuel
        self.distance = distance

    def start(self):
        print('Car Sound Boom Boom')

    def milage(self,fuel,distance):
        a=distance//fuel
        print(f"Your car provide mileage of {a} miles:",)




class Car(Vehicle):
    def __init__(self,fuel,distance):
        super().__init__(fuel,distance)

    def start(self):
        print('Jassi bhai is a game changer player')



x = Car("Mario","XL")
x.start()