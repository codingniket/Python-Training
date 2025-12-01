try:
    f = open("non_existent_file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: The file was not found.")
else:
    f = open("existent_file.txt", "w")
    print(f.write("Hello World"))
finally:
    print("Execution completed.")