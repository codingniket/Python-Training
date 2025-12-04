keys = [1,2,3,5,4]
values = [10,20,30,40,50]
d = {}
for i in range(len(keys)):
    if keys[i] not in d:
        d[keys[i]] = values[i]
    else:
        x = d[keys[i]]
        d[keys[i]] = [x,values[i]]

print(d)