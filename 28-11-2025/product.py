def printing():
    with open("products.txt","r") as file:
        content = file.read()
        x = content.split("\n")

    with open("catlog.txt","a") as file:
        file.write("Product     Price")
        for i in x:
            a,b = i.split(" ")
            file.write(item(a,b))


item = lambda product,price: f"\n{product}      {price}"
printing()