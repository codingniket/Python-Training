ip = input("Enter a sentence: ")
v , c , d = 0 , 0 , 0
for i in range(len(ip)):
    if ip[i] in 'aeiou' or ip[i] in 'AEIOU':
        v +=1
    elif ip[i].isdigit():
        d += 1
    elif ip[i] >= 'a' and ip[i] <= 'z' or ip[i] >= 'A' and ip[i] <= 'Z':
        c += 1
    else:
        print("Invalid Input")
        break

print(f"Number of vowels: {v}\nNumber of digits: {d}\nNumber of consonants: {c}")