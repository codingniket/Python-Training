
class WrongFileError(Exception):
    pass

filename = "example.txt"

try:
    if not filename.endswith(".csv"):
        raise WrongFileError("Incorrect File Type: Expected a .csv file")

    with open(filename, "r") as file:
        content = file.read()

except WrongFileError:
    print("Wrong File Type")

except FileNotFoundError:
    print("Reading file failed: File not found.")
