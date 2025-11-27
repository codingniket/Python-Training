with open("student.csv", "r") as f:
    content = f.read()
    x = content.split("\n")
    for i in x:
        print(i)