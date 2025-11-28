ip = input("Enter message/word: ")
def check(ip):
    j = len(ip)-1
    for i in range(len(ip) // 2):
        if ip[i] == ip[j]:
            j-=1
            continue
        else:
            print("Not a palindrome")
            return
    return True

if check(ip):
    print("Palindrome")
