try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Predefined exception in python 

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# Finally Keyword


try:
    f = open("non_existent_file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("Execution completed.")
    

try:
    num = int("50")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("It works")


def check_age(age):
    if age < 1:
        raise ValueError("Age cannot be negative.")
    else:
        print(f"Your age is {age}.")

check_age(5)

class LowBalanceError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds for this withdrawal.")
    return amount - balance

x = withdraw(150, 100)
print(f"Remaining balance: {x}")