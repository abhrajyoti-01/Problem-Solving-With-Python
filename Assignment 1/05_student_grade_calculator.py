def calculate_grade(percentage: float) -> str:
    if percentage > 85:
        return "A"
    if 75 <= percentage <= 85:
        return "B"
    if 50 <= percentage < 75:
        return "C"
    if 30 <= percentage < 50:
        return "D"
    return "Fail"


percentage = 82.5

if not 0 <= percentage <= 100:
    print("Please enter a percentage between 0 and 100.")
else:
    grade = calculate_grade(percentage)
    print(f"Grade: {grade}")
