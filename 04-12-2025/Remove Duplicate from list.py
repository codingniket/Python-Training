n = int(input("Enter the size of the list: "))
x = []
u = []
for i in range(n):
    x.append(int(input(f"Enter the prices: ")))
    if x[i] not in u:
        u.append(x[i])

print("All the unique values",u)