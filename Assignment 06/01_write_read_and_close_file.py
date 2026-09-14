with open("notes.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Python programming is simple.\nFile handling helps store data permanently.\n")

with open("notes.txt", "r", encoding="utf-8") as file_object:
    print("File contents:")
    print(file_object.read())

print("The file has been closed.")
