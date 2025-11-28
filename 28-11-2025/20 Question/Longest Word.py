ip = input("Enter message/word: ")
x = ip.split()
def longest_word(word):
    ans=""
    m=0
    for i in word:
        if len(i) > m:
            m = len(i)
            ans = i
    return ans

print(longest_word(x))