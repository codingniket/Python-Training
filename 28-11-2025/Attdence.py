
from datetime import datetime

def name(x,y):
    with open("attendance.log", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n{x} - {timestamp} - {y}")


ip = input("Enter your name and absent or present\n")
a,b = ip.split(" ")
name(a,b)
