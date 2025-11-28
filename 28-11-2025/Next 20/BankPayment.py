
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print(f"Processing payment of {self.amount}")


class CreditCardPayment(Payment):
    def process(self):
        print(f"Processing Credit Card payment of {self.amount}")


class UPIPayment(Payment):
    def process(self):
        print(f"Processing UPI payment of {self.amount}")


amount = int(input("Enter amount to pay: "))
print("Choose Payment Mode:\n1. Credit Card\n2. UPI")
choice = int(input("Enter choice: "))

if choice == 1:
    payment = CreditCardPayment(amount)
elif choice == 2:
    payment = UPIPayment(amount)
else:
    print("Invalid choice")
    payment = None

if payment:
    payment.process()
