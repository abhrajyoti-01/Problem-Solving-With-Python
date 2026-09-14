percentage = 82.5
grade = "A" if percentage > 85 else "B" if percentage >= 75 else "C" if percentage >= 50 else "D" if percentage >= 30 else "Fail"
print("Please enter a percentage between 0 and 100." if not 0 <= percentage <= 100 else f"Grade: {grade}")
