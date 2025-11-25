from enum import unique

x={1,1,3,3,4,2}
print(x)

empty = set()

s={1,2,3}

s.add(4)

print(s)

s.update([5,6])

print(s)
s.remove(1)
print(s)

s.discard(1)


print(s.pop())

a={1,2,3,4,5}
b={0,9,3}

print(a|b)
print(a&b)
print(a-b)
print(a^b)

unique1 = list(set(a))
print(unique1)