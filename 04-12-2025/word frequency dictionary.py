ip = input("Enter a sentence: ")

def count_words(ip):
    d = {}
    x = ip.split(" ")
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i,j in d.items():
        print(f"Frequency of {i} is {j}")

count_words(ip)