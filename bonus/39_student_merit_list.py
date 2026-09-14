count = int(input("How many students? "))
students = []

for i in range(count):
    name = input(f"\nName of student {i + 1}: ")
    students.append((name, float(input(f"Marks of {name}: "))))

students.sort(key=lambda item: item[1], reverse=True)

print("\nMerit list:")
for rank, (name, marks) in enumerate(students, start=1):
    print(f"{rank}. {name} - {marks:.1f}")

print(f"\nAverage marks: {sum(marks for _, marks in students) / count:.2f}")
print(f"Topper: {students[0][0]} ({students[0][1]:.1f})")
