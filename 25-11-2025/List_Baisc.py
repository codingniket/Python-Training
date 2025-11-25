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


fruit = ("Apple","Mango","Chawal")

print(fruit)
print(fruit[0])

print(fruit.count("M"))
print(fruit.index("Mango"))

print(fruit[1:3])
print(fruit[1:])
print(fruit[:3])
print(fruit[::-1])

nums=[10,20,30]
a,b,c = nums

print(a)
print(b)
print(c)



fruit = ("Apple","Mango","Chawal",("Lets","Go"))
print(fruit[3][1])


numbers=(1,34,5,0,243)
s = 1000
l=-1
for x in numbers:
    if x < s:
        s=x
    if x > l:
        l=x
print("Small Number",s,"Large Number",l)

