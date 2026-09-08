import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be 0).")
else:
    discriminant = b * b - 4 * a * c
    print(f"Discriminant: {discriminant}")
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two real roots: {root1:.2f} and {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"One repeated root: {root:.2f}")
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        print(f"Complex roots: {real:.2f} + {imaginary:.2f}i and {real:.2f} - {imaginary:.2f}i")
