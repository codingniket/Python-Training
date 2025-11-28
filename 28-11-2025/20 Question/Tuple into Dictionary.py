x = ("apple", "banana", "cherry")
d={}
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)
