
def log_error():
    e, w, c = 0, 0, 0
    with open("error.log", "r") as f:
        content = f.read()
        x = content.split("\n")
        for i in x:
            if "ERROR" in i:
                e+=1
            elif "WARNING" in i:
                w+=1
            elif "INFO" in i:
                c+=1
            else:
                pass

    with open("log_summary.txt", "w") as f:
        f.write(f"\nNumber of ERROR Lines {e}")
        f.write(f"\nNumber of INFO Lines {c}")
        f.write(f"\nNumber of WARNING Lines {c}")


log_error()