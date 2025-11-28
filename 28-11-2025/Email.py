def read():
    with open("students.txt","r") as f:
        content = f.read().strip().split("\n")
        for i in content:
            print(email(i))

email = lambda name: f'''
Dear {name},
Your training session starts tomorrow.
Regards,
Training Team
'''

read()