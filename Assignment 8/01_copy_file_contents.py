with open("data.txt", "w", encoding="utf-8") as file_object:
    file_object.write("This is the first line of data.\n")
    file_object.write("This is the second line of data.\n")

with open("data.txt", "r", encoding="utf-8") as source_file:
    content = source_file.read()

with open("backup.txt", "w", encoding="utf-8") as backup_file:
    backup_file.write(content)

with open("backup.txt", "r", encoding="utf-8") as backup_file:
    print(backup_file.read())
