ip = input("Enter message/word: ")
x = ip.split()
ans=[]
for i in x:
    if len(i)>=4:
        ans.append(i)

print(' '.join(ans))
