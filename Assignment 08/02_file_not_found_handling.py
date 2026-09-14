try:
    with open("missing_file.txt", "r", encoding="utf-8") as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("The file does not exist.")
