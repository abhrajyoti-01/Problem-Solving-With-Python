a, b = map(int, input("Enter two numbers: ").split())
print(f"Before swap: a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After swap (temp variable): a = {a}, b = {b}")

a, b = b, a
print(f"After swap (tuple swap):   a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b
print(f"After swap (arithmetic):    a = {a}, b = {b}")
