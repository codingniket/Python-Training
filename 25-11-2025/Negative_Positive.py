numbers = [-1,5,-6,2]
neg = []
pos=[]
for x in numbers:
    if x < 0:
        neg.append(x)
    else:
        pos.append(x)
neg.extend(pos)
print(neg)

