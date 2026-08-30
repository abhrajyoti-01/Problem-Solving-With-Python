a = 10
b = 5

print("Arithmetic operations")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")

print("\nLogical operations")
print(f"Logical AND (a > 0 and b > 0): {a > 0 and b > 0}")
print(f"Logical OR (a < 0 or b < 0): {a < 0 or b < 0}")
print(f"Logical NOT (not a < b): {not a < b}")

print("\nComparison operations")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a <= b: {a <= b}")

result = a + b * 2 - (a / b)
print(f"\nResult of expression a + b * 2 - (a / b): {result}")
