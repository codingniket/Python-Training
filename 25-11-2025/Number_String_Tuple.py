x=("Hey",1,"Time",2)
string=[]
number=[]
for i in x:
    if type(i)==str:
        string.append(i)
    else:
        number.append(i)

print("All String Tuple",string)
print("All number Tuple",number)