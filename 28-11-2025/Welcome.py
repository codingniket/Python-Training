def welcome(name,course):
    with open("welcome.txt",'a') as file:
        file.write(f"\nWelcome {name}!, to our college your course: {course}")

ip = input("Enter your name and course ")
a,b = ip.split(" ")
welcome(a,b)