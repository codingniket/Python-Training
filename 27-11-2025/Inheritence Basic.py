class Animal:
    def speak(self):
        print("My favorite animal")

class Dog(Animal):
    def color(self):
        print("I am black")

x = Dog()
x.color()
x.speak()


class Parent:
    def __init__(self,name):
        self.name = name

class Employee(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

x = Employee("Mario",25)
x.display()