nums = [10, 3, 5, 12, 8, 7, 1]
e=[]
o=[]
for num in nums:
    if num % 2 == 0:
        e.append(num)
    else:
        o.append(num)
print("Even",e)
print("Odd",o)