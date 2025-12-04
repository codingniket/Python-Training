a = {
    1: 10,
    2: 20,
    3: 30,
}

b = {
    1: 5,
    6: 40,
    7: 50,
}

for i,j in a.items():
    b[i] = b.get(i,0)+j

print(b)
