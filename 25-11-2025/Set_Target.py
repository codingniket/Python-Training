
numbers = {2, 4, 6, 8, 10}
target = 12

pairs = set()
for x in numbers:
    y = target - x
    if y in numbers:
        pair = tuple(sorted((x, y)))
        pairs.add(pair)
for p in pairs:
    print(p)
