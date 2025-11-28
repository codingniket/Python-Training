def generator(question):
    with open("questions.txt","a") as f:
        for item in range(len(question)):
            f.write(f"{item+1} {question[item]}\n ______ \n")

x = "Where is Taj Mahal?"
y = "Who Created it"
a = [x,y]
generator(a)
