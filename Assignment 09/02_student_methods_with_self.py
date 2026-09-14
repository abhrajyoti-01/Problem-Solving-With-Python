class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def print_grade(self):
        grade = "A" if self.marks >= 85 else "B" if self.marks >= 75 else "C" if self.marks >= 50 else "D" if self.marks >= 30 else "Fail"
        print(f"{self.name} secured grade {grade}.")


student = Student("Sourav", 4, 72)
student.print_grade()
student.update_marks(86)
print(f"Updated marks: {student.marks}")
student.print_grade()
