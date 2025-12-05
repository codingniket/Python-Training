from datetime import datetime,date,time, timedelta

today = date.today()
next = today + timedelta(days=7)
prev = today - timedelta(days=7)
print(today)
print(next)
print(prev)

print(today.year)
print(today.month)
print(today.day)

now = datetime.now()
print(now)


dob = datetime(1988,9,8)
print(dob)

format = now.strftime("%d-%m-%y %H:%M:%S")
print(format)

dt = datetime.combine(date(2027,7,6),time(10,5,1))
print(dt)

print((next - prev).days)