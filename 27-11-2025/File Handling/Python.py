words=[]
with open("backup.txt", "r") as f:
    content = f.read()
    y = content.split()
    for x in y:
        if "Python" in x:
            words.append(x)
    print("Number of words:", len(words))
