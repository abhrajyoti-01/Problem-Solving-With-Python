import os
with open("backup.txt", "w", encoding="utf-8") as file_object:
    file_object.write("This file will be renamed.\n")

if os.path.exists("data_backup.txt"):
    os.remove("data_backup.txt")

os.rename("backup.txt", "data_backup.txt")
print("backup.txt has been renamed to data_backup.txt")
