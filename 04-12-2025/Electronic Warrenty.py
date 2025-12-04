from datetime import datetime
from dateutil.relativedelta import relativedelta
class Product:
    def __init__(self,name,price,date):
        self.name = name
        self.price = price
        self.date = datetime.strptime(date, "%Y-%m-%d")

    def display(self):
        print(f"You have purchased {self.name} on {self.date.strftime('%Y-%m-%d')} at price of {self.price}")

class ElectronicProduct(Product):
    def __init__(self,name,price,date,warranty):
        Product.__init__(self,name,price,date)
        self.warranty = warranty

    def time(self):
        new_date = self.date + relativedelta(years=2)
        print(f"Warranty valid until: {new_date.strftime('%Y-%m-%d')}")



ep = ElectronicProduct("Laptop", 60000, "2023-12-04", 2)
ep.display()
ep.time()