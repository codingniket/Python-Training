ip = int(input("Enter the pos in 0 to 5"))
n = []
for i in range(5):
    n.append(int(input("Add this number to Array")))

ans = n[ip:]
ans.extend(n[0:ip])
print(ans)