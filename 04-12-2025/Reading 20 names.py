with open("Employee_Name.csv","w") as f:
    for i in range(20):
        x = input("Enter Employee Name: ")
        f.write(x+"\n")
d = {}
with open("Employee_Name.csv","r") as f:
    content = f.readlines()
    for idx, line in enumerate(content, start=1):
        d[idx] = line.strip()

print(d)
