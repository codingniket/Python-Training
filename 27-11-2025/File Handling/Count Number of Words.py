
with open("Notes.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Number of words:", len(words))
