def check(x):
    if x < 2:
        return False
    for j in range(2,x//2+1):
        if x%j==0:
            return False
        else:
            pass
    return True

n = int(input("Enter a start number: "))
z = int(input("Enter a end number: "))

for i in range(n,z+1):
    y = check(i)
    if y:
        print(i)
    else:
        pass

