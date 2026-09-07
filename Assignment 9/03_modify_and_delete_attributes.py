class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


student = Student("Priya", 5, 80)
print(f"Original name: {student.name}")

student.name = "Priya Sen"
student.roll = 15
print(f"Modified details: {student.name}, Roll {student.roll}")

del student.marks
try:
    print(student.marks)
except AttributeError:
    print("The marks attribute has been deleted.")

del student
try:
    print(student)
except NameError:
    print("The student object has been deleted.")
