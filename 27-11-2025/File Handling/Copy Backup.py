with open("Notes.txt", "r") as source_file:
    content = source_file.read()

with open("backup.txt", "w") as backup_file:
    backup_file.write(content)

print("Contents copied successfully!")
