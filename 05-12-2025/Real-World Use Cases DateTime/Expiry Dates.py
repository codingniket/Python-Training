from datetime import datetime, date
data = ['2025-09-10','2025-09-14','2025-09-24','2025-10-9','2025-12-30']
today = date.today()
for i in data:
    check = datetime.strptime(i, "%Y-%m-%d").date()
    if (check - today).days > 15:
        print(i)