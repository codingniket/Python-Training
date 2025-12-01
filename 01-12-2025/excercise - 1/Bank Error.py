class LowBalanceError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds for this withdrawal.")
    return amount - balance

x = withdraw(150, 100)
print(f"Remaining balance: {x}")