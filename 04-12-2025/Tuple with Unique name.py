x = ("orange","apple","pear", "banana", "orange")
y = set()
for i in x:
    if i not in y:
        y.add(i)
print(y)