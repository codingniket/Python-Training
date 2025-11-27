class Property :
    def __init__(self,age,year,space):
        self.age = age
        self.year = year
        self.space = space

    def built(self):
        print('Property Built on',self.year)
        print('Property Age is',self.age)

    def spaces(self):

        print("The space it was built on",self.space)


class Building (Property):
    def __init__(self,floor,age,year,space):
        super().__init__(age,year,space)
        self.floor = floor
    def floors(self):
        print(f"Building has {self.floor} floors")

class Apartment (Building):
    def __init__(self,floor,age,year,space,flat):
        super().__init__(floor,age,year,space)
        self.flat = flat
    def flat_number(self):
        print(f"Your flat number is {self.flat}")
        self.floors()
        self.built()
        self.spaces()


x = Apartment("2",12,2020,980,"B")
x.flat_number()