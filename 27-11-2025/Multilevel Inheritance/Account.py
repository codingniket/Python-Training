class Account :
    def __init__(self,bank,address):
        self.bank = bank
        self.address = address

    def opening(self):
        print(f'Your bank is {self.bank} and address is {self.address}')

    def safety(self):
        print("Please follow the instructions to open the account")


class DigitalAccount (Account):
    def __init__(self,bank,address,date):
        super().__init__(bank,address)
        self.date = date
    def joining(self):
        print(f"Your account opening Date is {self.date}")

class PremiumAccount (DigitalAccount):
    def __init__(self,bank,address,date,networth):
        super().__init__(bank,address,date)
        self.networth = networth
    def display(self):
        self.safety()
        self.opening()
        self.joining()
        print(f"As per your networth {self.networth} you have a premium account")


x = PremiumAccount("HD","Dolakpur","2020/11/1",9800,)
x.display()