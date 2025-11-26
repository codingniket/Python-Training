import math
class Mobile:
    def __init__(self,brand:str,model:str,storage:int):
        self.brand = brand
        self.model = model
        self.storage = storage

    def upgrade(self):
        curr = int(math.log(self.storage,2))
        self.storage = 2**(curr+1)
        self.display("New Storage (in GB)")

    def display(self, text):
        print(f"{text}",self.storage)


user1 = Mobile("Samsung","M12",32)
user1.display("Current Storage (in GB)")
user1.upgrade()

