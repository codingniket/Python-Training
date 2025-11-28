n = int(input("Enter a number: "))
x = []
for i in range(n):
    ip = int(input("Enter a number: "))
    x.append(ip)
s = list(filter(lambda y: y%2 == 0,x))
print(s)
