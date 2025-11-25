nums = [5, 2, 7, 5, 9, 5, 3]
ip = int(input("Enter the number to find: "))
ans = []
for i in range(len(nums)):
    if nums[i] == ip:
        ans.append(i)
print(ans)