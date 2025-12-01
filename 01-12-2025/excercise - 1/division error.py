try:
    x = input("Enter two number: ")
    a,b = x.split(" ")
    int(a) / int(b)
except ZeroDivisionError:
    print("You can't divide by zero")
