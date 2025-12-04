x = [("orange", 1), ("apple", 2), ("pear", 3), ("banana", 4), ("orange", 5)]
d={}
for i in x:
    x,y = i
    if x in d:
        d.pop(x)
    else:
        d[x]=y
print(d)