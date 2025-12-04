c,w,l = 0,0,0
with open("text","r") as f:
    content = f.readlines()
    l = len(content)
    text = " ".join(content)
    check = text.split(" ")
    for i in check:
        w += 1
        c += len(i)
print("Number of characters: ",c)
print("Number of words: ",w)
print("Number of letters: ",l)