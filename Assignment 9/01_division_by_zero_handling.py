numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    result = numerator / denominator
    print(f"Result = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
