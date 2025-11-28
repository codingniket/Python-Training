
from datetime import datetime

def name(x,y):
    with open("attdence.log", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n{x} - {timestamp} - {y}")


ip = input("Enter your name and abesnt or present\n")
a,b = ip.split(" ")
name(a,b)
