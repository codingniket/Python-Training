s = lambda x: x*x
print(s(5))

add = lambda x, y: x + y
print(add(3,4))

generate_line = lambda user: f"Hello {user}, Welcome to EY GDS"

def write_dynamic(name,filename):
    with open(filename,"w") as f:
        f.write(generate_line(name))

write_dynamic("John","user.txt")


details = lambda name,age,salary : f'''
Username: {name}
Password: {age}
Salary: {salary}
'''
def employee(name,age,salary,filename):
    with open(filename,"a") as f:
        f.write(details(name,age,salary))

employee("John",22,"Salary","user.txt")