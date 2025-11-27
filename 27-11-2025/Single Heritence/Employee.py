class Company:
    def __init__(self,department,rank):
        self.department = department
        self.rank = rank

    def dept_info(self):
        print(self.department)
        print(self.rank)

    def working_hour(self,name):
        print(f"{name} you need to work 8 hours a day")


class Employee(Company):
    def __init__(self,name,age,location,department,rank):
        super().__init__(department,rank)
        self.name = name
        self.age = age
        self.location = location
    def display(self):
        print(self.name)
        print(self.age)
        print(self.location)
        self.dept_info()
        self.working_hour(self.name)

x = Employee("Mario",25,"India","IT",44)
x.display()