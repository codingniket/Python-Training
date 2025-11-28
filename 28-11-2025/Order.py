def invoice():
    s = 0
    with open("orders.csv",'r') as f:
        content = f.read()
        x = content.strip().split("\n")
        for i in x:
            a,b,c = i.split(",")
            s+=int(c)*int(b)
            print(bill(a,b,c))
    print("Total Payable =",s)


bill = lambda name,qty,price: f"{name} = {qty} x {price}"
invoice()