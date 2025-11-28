class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)

x = Employee("Bob",12,10000)
x.display()