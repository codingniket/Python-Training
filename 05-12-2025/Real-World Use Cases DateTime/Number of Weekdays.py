from datetime import datetime, timedelta

date1_str = input("Enter your first date in yyyy-mm-dd format: ")
date2_str = input("Enter your second date in yyyy-mm-dd format: ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")


weekday_count = 0
current_date = date1
while current_date <= date2:
    if current_date.weekday() < 5:
        weekday_count += 1
    current_date += timedelta(days=1)

print("Number of weekdays between the two dates:", weekday_count)