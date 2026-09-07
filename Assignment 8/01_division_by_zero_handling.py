numerator = 10.0
denominator = 0.0

try:
    result = numerator / denominator
    print(f"Result = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
