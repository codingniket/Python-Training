x={"A": 85, "B": 92, "C": 78, "D": 92}
m = 0
c=""
for i,j in x.items():
    if j > m:
        m = j
        c=i
print(c)