# Create a Payment class with credit-card and UPI subclasses overriding process_payment().

class Payment:
    def __init__(self,amount,payment):
        self.amount = amount
        self.payment = payment

    def process_payment(self):
        if self.amount < self.payment:
            print("Payment Error, You don't have enough money")

class CreditCard(Payment):
    def __init__(self,amount,payment):
        super().__init__(amount,payment)

    def process_payment(self):
        print("Paid Successfully: Remaining Balance",(100000 - self.payment))

class UPI(Payment):
    def __init__(self,amount,payment):
        super().__init__(amount,payment)
    def process_payment(self):
        if self.amount < self.payment:
            print("Not enough balance")

        return self.amount - self.payment

x = CreditCard(100,1000)
x.process_payment()

x = UPI(10000,5000)
print("Current Balance",x.process_payment())