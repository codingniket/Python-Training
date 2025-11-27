class AmazonPayment:
    def __init__(self, balance,credit_card_balance):
        self.balance = balance
        self.credit_card_balance = 1000


    def debit_card(self, amount):
        if self.balance < amount:
            print("Not enough money")
            return
        self.balance -= amount
        self.display()

    def upi(self, amount):
        if self.balance < amount:
            print("Not enough money")
            return
        self.balance -= amount
        self.display()

    def credit_card(self,amount):
        if self.credit_card_balance < amount:
            print("You don't have enough balance")
        self.credit_card_balance -= amount
        print(f"{amount} debited successfully")
        print(f"{self.credit_card_balance} Credit Card Balance")

    def display(self):
        print("Current balance:",self.balance)

    def switch(self,n:int):
        print("Enter amount to Debit")
        y = int(input())
        if n == 1:
            self.debit_card(y)
        elif n == 2:
            self.credit_card(y)
        elif n == 3:
            self.upi(y)
        else:
            print("Invalid Choice Please try again later")

n1 = int(input("Enter starting Balance:"))
x = AmazonPayment(n1,0)
x.display()
y = int(input("Enter Payment Mode \n 1.Debit Card \n 2.Credit Card \n 3.UPI \n"))
x.switch(y)