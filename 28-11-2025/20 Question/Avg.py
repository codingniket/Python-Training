def average(x):
    y = len(x)
    z = sum(x)
    return z//y
a = []
n = int(input("Enter how many inputs you want: "))
for i in range(n):
    ip = int(input("Enter a number: "))
    a.append(ip)
print(average(a))

