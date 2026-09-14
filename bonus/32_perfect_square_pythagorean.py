from math import isqrt


def is_perfect_square(number):
    return number >= 0 and isqrt(number) ** 2 == number


number = int(input("Enter a number to check if it is a perfect square: "))
print(f"{number} is {'a' if is_perfect_square(number) else 'not a'} perfect square.")

a, b, c = map(int, input("Enter three integers for Pythagorean triple check: ").split())
sides = sorted((a, b, c))
print(f"({a}, {b}, {c}) {'is' if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 else 'is not'} a Pythagorean triple.")
