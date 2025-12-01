x = ["1","2","3","a"]

for i in x:
    try:
        y = int(i)
        print(y)
    except ValueError:
        print("Please enter a valid integer.")
