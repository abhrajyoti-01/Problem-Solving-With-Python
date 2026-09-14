numerator, denominator = 10.0, 0.0

try:
    print(f"Result = {numerator / denominator}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
