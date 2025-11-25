nums = [0, 3, 0, 5, 7, 0, 9]
c = 0
ans=[]
for num in nums:
    if num == 0:
        c+=1
    else:
        ans.append(num)
x = [0]*c
ans.append(x)
print(ans)