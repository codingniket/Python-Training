
try:
    with open("sample.txt", "r") as f:
        data = f.read()
    print("File content:", data)

    try:
        with open("sample.txt", "w") as f:
            f.write("PeaceMaker")
        print("Write successful")
    except PermissionError:
        print("Permission error while writing")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error while reading")
