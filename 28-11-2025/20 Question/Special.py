ip = input("Enter message/word: ")
ans=[]
for i in range(len(ip)):
    if ord(ip[i]) >= 65 and ord(ip[i]) <= 90 or ord(ip[i]) >= 97 and ord(ip[i]) <= 122:
        ans.append(ip[i])
print(''.join(ans))
