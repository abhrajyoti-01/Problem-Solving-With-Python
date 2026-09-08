a, b = map(int, input("Enter two numbers: ").split())
print(f"Before swap: a = {a}, b = {b}")

# Method 1: Using a temporary variable
temp = a
a = b
b = temp
print(f"After swap (temp variable): a = {a}, b = {b}")

# Method 2: Pythonic tuple swap (swap back)
a, b = b, a
print(f"After swap (tuple swap):   a = {a}, b = {b}")

# Method 3: Using arithmetic operators
a = a + b
b = a - b
a = a - b
print(f"After swap (arithmetic):    a = {a}, b = {b}")
