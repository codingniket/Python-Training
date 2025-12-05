from datetime import datetime, timedelta

ip = input("Enter your delivery start date in yyyy-mm-dd format: ")
check = datetime.strptime(ip, "%Y-%m-%d").date()

days = 3

estimated_delivery = check + timedelta(days=days)

print(f"Estimated delivery date: {estimated_delivery}")