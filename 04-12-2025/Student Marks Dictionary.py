marks = {
    "Rajesh" : 50,
    "Bob" : 90,
    "Randy" : 32,
    "Edge": 78,
    "Roman" : 65,
    "Seth" : 85,
}
sorted_dict = sorted(marks.items(),key = lambda item: item[1],reverse = True)
last_three = dict(sorted_dict[:3])
print("Top 3 Rankers",last_three)



