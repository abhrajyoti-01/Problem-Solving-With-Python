with open("pointer.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Python file pointer")

with open("pointer.txt", "r", encoding="utf-8") as file_object:
    print(f"Initial pointer position: {file_object.tell()}")
    print(f"First 6 characters: {file_object.read(6)}")
    print(f"Pointer after reading 6 characters: {file_object.tell()}")
    file_object.seek(7)
    print(f"Pointer after seek(7): {file_object.tell()}")
    print(f"Data from position 7: {file_object.read()}")
