class Mammal:
    def sound(self):
        print("Mammal")

class Dog(Mammal):
    def sound(self):
        print("Bark Bark")

class Cat(Mammal):
    def sound(self):
        print("Mio Mio")


x = Dog()
x.sound()

y = Cat()
y.sound()