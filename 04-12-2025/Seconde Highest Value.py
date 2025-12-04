n = int(input("Enter a number:"))
x = []
m,s=0,0
for i in range(n):
    x.append(int(input(f"Enter {n} number:")))
    if x[i]>m:
        s=m
        m=x[i]
    elif s < x[i] < m:
        s=x[i]
print("The seconde largest number is ",s)
