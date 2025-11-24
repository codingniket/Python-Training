print("Hello World!")
name="Niket"
age = 22
salary = 4.5
print(f"My name {name}, my age {age} and salary {salary}")
a=10
b=4

print("Add",a+b)
print("Subz",a-b)
print("Div",a/b)
print("Floor Div",a//b)
print("Mod",a%b)
print("Power",a**b)

for i in range(1,21):
    if i%2 == 0:
        print(i," is Even")
    else:
        print(i," is Odd")
        
# If - else

marks = int(input("Enter a number "))

if marks >= 90:
    print("Grade A")
elif marks >= 60 and marks < 90:
    print("Grade B")
else:
    print("Grade C")
    
for i in range(1,6):
    print("Number = ",i)
    
    
counter = 1
while counter != 5:
    print("Counter = ", counter)
    counter += 1