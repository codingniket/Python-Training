x = (1,2,3,2)
m,s=0,0
for i in range(len(x)):
    if x[i]>m:
        s = m
        m=x[i]

    elif m > x[i] > s:
        s=x[i]
    else:
        pass
print("Seconde Largest in Tuple",s)
