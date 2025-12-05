class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private variable

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def get_balance(self):
        print(self.__balance)


acc = BankAccount("Shark",800)
acc.get_balance()
acc.deposit(500)
acc.withdraw(100)
acc.__balance = 100000
acc.get_balance()
print(dir(acc))