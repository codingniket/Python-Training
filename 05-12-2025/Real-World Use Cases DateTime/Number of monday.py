from datetime import datetime, timedelta
data = ['2025-09-10','2025-09-14','2025-09-24','2025-10-9','2025-12-01']
monday = 0
for i in data:
    check = datetime.strptime(i, "%Y-%m-%d")
    if check.weekday() == 0:
        monday += 1
print("Number of monday :", monday)