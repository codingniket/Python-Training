
t = (10, (20, 30), (40, (50, 60)))
ans=[]

def unplug(x):
    y=[]
    for i in x:
        if type(i)==tuple:
            z=unplug(i)
            y.extend(z)
        else:
            y.append(i)
    return y

for i in t:
    if type(i) is tuple:
        ans.extend(unplug(i))
    else:
        ans.append(i)

ans.sort(reverse=True)
print(ans)

