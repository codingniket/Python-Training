class Bank:
    def __init__(self,cus_id:str,name:str,balance:int):
        self.cus_id = cus_id
        self.name = name
        self.balance = balance
    def withdraw(self,amount:int):
        if self.balance < amount:
            print("Not enough money")
        self.balance -= amount
        self.display_balance("After Withdrawn")

    def deposit(self,amount:int):
        self.balance += amount
        self.display_balance("After Deposit")

    def check_balance(self):
        self.display_balance("")

    def display_balance(self, text):
        print("Current Balance: ",text,self.balance)

user1 = Bank("101","Saman",100)
user1.deposit(50)
user1.check_balance()
user1.withdraw(20)
user1.check_balance()
