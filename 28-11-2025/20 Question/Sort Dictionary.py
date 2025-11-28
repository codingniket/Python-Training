people = [
    {"name": "A", "age": 30},
    {"name": "B", "age": 25},
]

# Sort by age using lambda
people.sort(key=lambda x: x["age"])

print(people)
