d = {}
ip = input("Enter message/word: ")

for i in range(0,len(ip)):
    if ip[i] in d:
        d[ip[i]] += 1
    else:
        d[ip[i]] = 1

for i,j in d.items():
    print(f"{i} has appeared {j} times")