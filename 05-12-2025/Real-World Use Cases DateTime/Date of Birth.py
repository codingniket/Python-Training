from datetime import datetime, timedelta, date

ip = input("Enter your delivery start date in yyyy-mm-dd format: ")

check = datetime.strptime(ip, "%Y-%m-%d").date()
today = date.today()

year = today.year-check.year
month = today.month-check.month
day = today.day-check.day

print(f"You are this {year} year- {month} -month {day} day old")