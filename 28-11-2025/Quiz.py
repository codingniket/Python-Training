def generator(question):
    with open("questions.txt","a") as f:
        for item in range(len(question)):
            f.write(f"{item+1} {question[item]}\n ______ \n")

x = "Who is Bob?"
y = "Why is Bob here"
a = [x,y]
generator(a)
