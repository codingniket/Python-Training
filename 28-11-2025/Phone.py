def printing():
    with open("contact.csv","r") as file:
        content = file.read()
        x = content.split()
        print(x)

    with open("contacts_export.txt","w") as file:
        for i in x:
            a,b = i.split(",")
            file.write(item(a,b))


item = lambda name,num: f'''
Name: {name} | Phone: {num}
'''
printing()