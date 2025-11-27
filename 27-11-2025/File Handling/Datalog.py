
from datetime import datetime

with open("app.log", "w") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"{timestamp} - Application started\n")

print("Log entry added!")
