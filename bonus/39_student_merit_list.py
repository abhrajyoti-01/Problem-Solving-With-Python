count = int(input("How many students? "))
students = []

for i in range(count):
    name = input(f"\nName of student {i + 1}: ")
    marks = float(input(f"Marks of {name}: "))
    students.append((name, marks))

students.sort(key=lambda item: item[1], reverse=True)

print("\nMerit list:")
for rank, (name, marks) in enumerate(students, start=1):
    print(f"{rank}. {name} - {marks:.1f}")

average = sum(marks for _, marks in students) / count
topper_name, topper_marks = students[0]
print(f"\nAverage marks: {average:.2f}")
print(f"Topper: {topper_name} ({topper_marks:.1f})")
