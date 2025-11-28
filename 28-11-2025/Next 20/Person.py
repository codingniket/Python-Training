class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def retirement(self):
        print(f"Retirement age remaining is {60-self.age}")

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def pay(self):
        print(f"My company pays {self.salary} to me per month")

class Manager(Employee):
    def __init__(self,name,age,salary,rank):
        super().__init__(name,age,salary)
        self.rank = rank

    def display(self):
        print("My rank",self.rank)
        self.pay()
        self.retirement()

x = Manager("Mario",40,100, 440)
x.display()


