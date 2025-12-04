salary = {
    "Rajesh" : 50000,
    "Bob" : 90000,
    "Randy" : 3000,
    "Edge": 78000,
    "Roman" : 65000,
    "Seth" : 85000,
}

x = dict(filter(lambda item: item[1] > 60000,salary.items()))
print(x)
