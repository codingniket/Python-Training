def invoice(a,b,c):
    s = 0
    with open("order_summary.txt",'w') as f:
        s+=int(c)*int(b)
        f.write(bill(a,b,c))
        f.write(f"\nTotal Payable = {s}")



bill = lambda name,qty,price: f"{name} = {qty} x {price}"

x = input("Enter your name qty item")
a,b,c = x.split(" ")
invoice(a,b,c)