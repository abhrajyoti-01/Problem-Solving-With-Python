file_name = 'missing_file.txt'

try:
    with open(file_name, "r", encoding="utf-8") as file_object:
        print(file_object.read())
except FileNotFoundError:
    print("The file does not exist.")
