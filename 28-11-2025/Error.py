from datetime import datetime
def log_error(message):
    with open("error.log", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n{message} - {timestamp}")

for i in range(5):
    ip= input("Enter error message: ")
    log_error(ip)