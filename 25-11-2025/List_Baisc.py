l = [10,20,30,40]

print(l[1:3])
print(l[1:])
print(l[:3])
print(l[::-1])

print(len(l))
print(max(l))
print(min(l))

l.reverse()

print(l)
l.sort(reverse=True)
print(l)

print([n*n for n in l]) #list comprehension