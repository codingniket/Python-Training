with open("students.txt","r") as f:
    content = f.read()
    x = content.split("\n")
    for i in x:
        print(f"Thank you for participation {i}")