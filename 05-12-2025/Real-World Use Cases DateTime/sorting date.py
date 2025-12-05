from datetime import datetime
data = ['2025-09-10','2025-09-14','2025-09-24','2025-10-9','2025-12-30']
x=[]
for i in data:
    check = datetime.strptime(i, "%Y-%m-%d").date()
    x.append(check)
print(sorted(x))