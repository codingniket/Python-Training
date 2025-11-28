x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

ans={}

def add(x):
    for i in x:
        if i in ans:
            z = ans[i]
            ans[i] = [x[i],z]
        else:
            ans[i] = x[i]


add(x)
add(y)
print(ans)