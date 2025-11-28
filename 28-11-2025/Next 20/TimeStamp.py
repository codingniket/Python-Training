
from datetime import datetime


with open("./txt/sample.txt", "a") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f" {timestamp}")



