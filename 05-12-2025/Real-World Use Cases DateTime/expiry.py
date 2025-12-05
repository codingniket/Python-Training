from datetime import datetime, timedelta
ip = input("Enter your date in yyyy-mm-dd format: ")
days = input("Enter duration in days")
y,m,d = ip.split("-")
curr = datetime(int(y),int(m),int(d))
expiry = (curr + timedelta(days=int(days))).strftime("%Y-%m-%d")
print("Expiry Date ",expiry)