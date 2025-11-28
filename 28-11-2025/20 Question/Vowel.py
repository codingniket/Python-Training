def vowel(x):
    ans=[]
    for i in range(len(x)):
        if x[i] in 'aeiou' or x[i] in 'AEIOU':
            pass
        else:
            ans.append(x[i])
    return ''.join(ans)


n = input("Enter a string: ")
print(vowel(n))

