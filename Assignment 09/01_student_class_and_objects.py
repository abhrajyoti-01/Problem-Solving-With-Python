class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")


for student in (Student("Ananya", 1, 88), Student("Rohan", 2, 76), Student("Meera", 3, 91)):
    student.display()
