
with open("numbers.txt", "w") as f:
    for x in range (1,11):
        f.write(str(x**2)+"\n")
