from datetime import datetime
def log_error(message):
    with open("data.log", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n{message} - {timestamp}")

for i in range(3):
    ip= input("Enter message for logging: ")
    log_error(ip)