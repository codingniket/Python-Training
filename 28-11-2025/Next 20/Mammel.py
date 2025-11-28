class Mammel:
    def sound(self):
        print("Zindagi ki saath zindagi ka baad bhi")

class Dog(Mammel):
    def sound(self):
        print("Bark Bark")

class Cat(Mammel):
    def sound(self):
        print("Miow Moiw")


x = Dog()
x.sound()

y = Cat()
y.sound()