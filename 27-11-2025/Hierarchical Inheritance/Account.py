class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"[Account] {self.owner} deposited {amount}. Balance: {self.balance}")


class SavingsAccount(Account):
    def add_interest(self, rate=0.04):
        interest = self.balance * rate
        self.balance += interest
        print(f"[SavingsAccount] Interest {interest} added. Balance: {self.balance}")


class CurrentAccount(Account):
    def withdraw(self, amount):
        # Overdraft allowed up to 500 for demo purposes
        if amount > self.balance + 500:
            print("[CurrentAccount] Overdraft limit exceeded!")
            return False
        self.balance -= amount
        print(f"[CurrentAccount] Withdrew {amount}. Balance: {self.balance}")
        return True


class SalaryAccount(Account):
    def apply_salary(self, amount):
        self.deposit(amount)
        print(f"[SalaryAccount] Salary {amount} credited.")


sav = SavingsAccount("Shubham", 1000)
sav.add_interest()
cur = CurrentAccount("Avinandan", 200)
cur.withdraw(600)
sal = SalaryAccount("Dipanjan", 0)
sal.apply_salary(50000)


# Example 2: Payment → CreditCardPayment, UPIPayment, WalletPayment

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        raise NotImplementedError("Subclasses must implement process()")


class CreditCardPayment(Payment):
    def process(self, card_number):
        print(f"[Card] Charged ₹{self.amount} to card ****{str(card_number)[-4:]}")


class UPIPayment(Payment):
    def process(self, upi_id):
        print(f"[UPI] Paid ₹{self.amount} via UPI ID {upi_id}")


class WalletPayment(Payment):
    def __init__(self, amount, wallet_balance):
        super().__init__(amount)
        self.wallet_balance = wallet_balance

    def process(self):
        if self.amount > self.wallet_balance:
            print("[Wallet] Insufficient wallet balance!")
            return False
        self.wallet_balance -= self.amount
        print(f"[Wallet] Paid ₹{self.amount}. Remaining wallet balance: ₹{self.wallet_balance}")
        return True


cc = CreditCardPayment(1299)
cc.process("4111111111111111")
upi = UPIPayment(799)
upi.process("ok@okaxis")
wallet = WalletPayment(500, wallet_balance=1200)
wallet.process()