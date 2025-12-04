class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

acc1 = BankAccount(1000)
acc2 = BankAccount(2000)

print(acc1 + acc2)