def is_perfect_square(number):
    if number < 0:
        return False
    root = int(number**0.5)
    for candidate in (root - 1, root, root + 1):
        if candidate >= 0 and candidate * candidate == number:
            return True
    return False


def is_pythagorean_triple(a, b, c):
    sides = sorted((a, b, c))
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


number = int(input("Enter a number to check if it is a perfect square: "))
print(f"{number} is {'a' if is_perfect_square(number) else 'not a'} perfect square.")

a, b, c = map(int, input("Enter three integers for Pythagorean triple check: ").split())
print(f"({a}, {b}, {c}) {'is' if is_pythagorean_triple(a, b, c) else 'is not'} a Pythagorean triple.")
