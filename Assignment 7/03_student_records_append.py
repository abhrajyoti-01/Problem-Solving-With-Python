with open("student.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Name,Marks\n")
    file_object.write("Abhra,83\n")
    file_object.write("Mohit,76\n")

with open("student.txt", "a", encoding="utf-8") as file_object:
    file_object.write("Meera,91\n")
    file_object.write("Sourav,69\n")

with open("student.txt", "r", encoding="utf-8") as file_object:
    print(file_object.read())
