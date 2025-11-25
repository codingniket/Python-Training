nums = [10, 11, 12, 13, 17, 20, 23]
def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
ans=[]
for num in nums:
    if prime(num):
        ans.append(num)
print(ans)