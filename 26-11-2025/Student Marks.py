class Student:
    def __init__(self,name:str,m1:int,m2:int,m3:int):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def marks(self):
        return self.m1+self.m2+self.m3

    def percentage(self):
        return round(self.marks()/300*100,2)

    def display(self):
        print("Student Name:",self.name)
        print("Marks per subject",self.m1,self.m2,self.m3)
        print("Marks Obtained:",self.marks())
        print("Percentage:",self.percentage())

calculator = Student("Bob",81,23,78)
calculator.display()
