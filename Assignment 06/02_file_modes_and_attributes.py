def show_details(file_object):
    print("Mode:", file_object.mode)
    print("Name:", file_object.name)
    print("Closed:", file_object.closed)
    print("Readable:", file_object.readable())
    print("Writable:", file_object.writable())


file_object = open("modes.txt", "w", encoding="utf-8")
file_object.write("First line\n")
show_details(file_object)
file_object.close()
print()

file_object = open("modes.txt", "r", encoding="utf-8")
show_details(file_object)
file_object.close()
print()

file_object = open("modes.txt", "a", encoding="utf-8")
file_object.write("Second line\n")
show_details(file_object)
file_object.close()
print()

file_object = open("modes.txt", "r+", encoding="utf-8")
show_details(file_object)
file_object.close()
