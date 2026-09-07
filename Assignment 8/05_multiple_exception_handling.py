print("Choose an option:")
print("1. IndexError")
print("2. TypeError")
print("3. FileNotFoundError")

choice = '1'

try:
    if choice == "1":
        values = [10, 20, 30]
        print(values[5])
    elif choice == "2":
        print(10 + "20")
    elif choice == "3":
        with open("missing_file.txt", "r", encoding="utf-8") as file_object:
            print(file_object.read())
    else:
        print("Invalid choice.")
except IndexError:
    print("IndexError occurred and was handled.")
except TypeError:
    print("TypeError occurred and was handled.")
except FileNotFoundError:
    print("FileNotFoundError occurred and was handled.")
