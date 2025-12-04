class Students:
    def __init__(self,id,name,maths,science,history):
        self.name = name
        self.maths = maths
        self.science = science
        self.history = history
        self.id = id
    def grade(self):
        return (self.maths+self.science+self.history)/300
    def display(self):
        print("Marks received",self.maths+self.science+self.history)
        print("Percentage",round(self.grade()*100,2),"%")

x = Students(1,"John Doe",89,78,90)
x.display()