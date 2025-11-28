def expense_items(name, amount):
    with open("report.txt","w") as f:
        f.write(f"Product - {name} Amount - {amount}\n")


x = input("Enter the product name and amount \n")
n,a = x.split(" ")
expense_items(n,a)