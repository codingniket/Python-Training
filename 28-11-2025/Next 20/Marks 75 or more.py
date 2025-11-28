with open("./txt/marks.csv", "r") as f:
    content = f.read()
    y = content.split()
    for x in y:
        a,b = x.split(",")
        if int(b) > 75:
            print(f"Name {a} Marks {b}")
