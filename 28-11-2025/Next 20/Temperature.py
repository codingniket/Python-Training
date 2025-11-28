class Temperature:
    def __init__(self,temp):
        self.temp = temp
    def fehrenhite(self):
        return self.temp * 9/5 + 32
    def celcheline(self):
        return  5/9*(self.temp - 32)
    def display(self):
        print(self.fehrenhite())
    def display2(self):
        print(self.celcheline())


n = int(input("In which temp you want 1. Ferenhite 2.Celicus \n"))
if n == 2:
    x = Temperature(int(input("What is the temperature? in C \n")))
    x.display()
else:
    x = Temperature(int(input("What is the temperature? in F \n")))
    x.display2()

