from datetime import datetime, date

ip = input("Enter your date in yyyy-mm-dd format: ")

check = datetime.strptime(ip, "%Y-%m-%d").date()
today = date.today()

if today == check:
    print("Today is in the present day")
elif today > check:
    print("Date is from past")
else:
    print("Date is from future")