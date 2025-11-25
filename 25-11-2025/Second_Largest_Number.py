nums = [23, 89, 12, 78, 55, 42]
l,s = 0,0
for num in nums:
    if num > l:
        s=l
        l = num
    if num < l and num > s:
        s = num
print("second largest number",s)