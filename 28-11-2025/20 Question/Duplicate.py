numbers = [1, 2, 3, 2, 4, 1, 5, 1]
d={}
for i in numbers:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

ans=[]
for i,j in d.items():
    if j > 1:
        # print(i)
        ans.append(i)
print(ans)