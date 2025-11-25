nums = [0, 3, 0, 5, 7, 0, 9]
l = len(nums)
ans=[0]*l
c=0
for i in range(l):
    if nums[i] != 0:
        ans[c]=nums[i]
        c+=1

print(ans)