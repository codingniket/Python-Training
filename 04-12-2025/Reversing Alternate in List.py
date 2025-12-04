x = ["I", "live" , "in", "India", "with", "my" , "family"]
ans = []
for i in range(len(x)):
    if i%2 == 1:
        rev = x[i]
        rev = rev[::-1]
        ans.append(rev)
    else:
        ans.append(x[i])
print(ans)