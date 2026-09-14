with open("student.txt", "w", encoding="utf-8") as file_object:
    file_object.write("Name,Marks\nAbhra,83\nMohit,76\n")

with open("student.txt", "a", encoding="utf-8") as file_object:
    file_object.write("Meera,91\nSourav,69\n")

with open("student.txt", "r", encoding="utf-8") as file_object:
    print(file_object.read())
