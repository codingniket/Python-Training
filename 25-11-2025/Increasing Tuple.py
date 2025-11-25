num=(1,3,5,6)

for i in range(1,len(num)):
    if num[i] > num[i-1]:
        pass
    else:
        print("Not increasing")
        break
print("Increasing")