file_object = open("notes.txt", "w", encoding="utf-8")
file_object.write("Python programming is simple.\n")
file_object.write("File handling helps store data permanently.\n")
file_object.close()

file_object = open("notes.txt", "r", encoding="utf-8")
print("File contents:")
print(file_object.read())
file_object.close()

print("The file has been closed.")
