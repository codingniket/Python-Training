# Student Class
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def check(self):
        print(self.name)
        print(self.age)
        return "Hey"
s1 = Student("Bot",20)
print(s1.check())

# Car Class
class Car:
    def __init__(self,modal:str,brand:str,year:int):
        self.modal= modal
        self.brand= brand
        self.year = year
    def display(self):
        print(f"Your car modal is {self.brand} {self.modal} and year is {self.year}")
    def price_calculator(self,insurance:int) -> int:
        price = (self.year / 10) + insurance + 30000
        return int(price)

ford = Car("Eco Sport","Ford",2020)
ford.display()
print(ford.price_calculator(10000))

#Employee
class Employee:
    def __init__(self,emp_id:str,name:str,department:str,salary:int):
        self.emp_id= emp_id
        self.name = name
        self.department = department
        self.salary = salary
    def display(self):
        print(self.name,end="   ")
        print(self.department,end="     ")
        print(self.salary,end="     ")
        print(self.emp_id,end="     ")
    def table_print(self):
        print("Name  Dept  Salary  Emp_ID")


e1 = Employee("101","Sama","IT",100)
e2 = Employee("102","Elon","IT",200)
e1.table_print()
e1.display()
print()
e2.display()
