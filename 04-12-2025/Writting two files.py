with open("data.log","r") as f:
    content = f.readlines()

mid = len(content)//2

with open("input1.txt","w") as f:
    f.writelines(content[:mid])

with open("input2.txt","w") as f:
    f.writelines(content[mid:])

print("Added both these files")