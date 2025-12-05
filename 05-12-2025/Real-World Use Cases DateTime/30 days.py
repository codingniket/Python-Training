from datetime import datetime, timedelta, date

today = date.today()

for i in range(30):
    estimated_delivery = today + timedelta(days=i)
    print(estimated_delivery)

