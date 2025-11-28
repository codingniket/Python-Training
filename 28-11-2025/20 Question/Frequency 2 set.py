y = set()
n = int(input("Enter a number: "))
x = []
for i in range(n):
    ip = int(input("Enter a number: "))
    x.append(ip)

for i in x:
    if i not in y and x.count(i) ==  2:
        y.add(i)
        print(i,end="")

