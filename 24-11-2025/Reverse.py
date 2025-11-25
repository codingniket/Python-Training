a = int(input("Enter number:"))
s=0
while a>0:
    d= a%10
    s = (s*10) + d
    a=a//10
print("Reverse",s)