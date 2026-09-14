from math import factorial


def is_strong(number):
    total = sum(factorial(int(digit)) for digit in str(number)) if number > 0 else 0
    return total == number


number = int(input("Enter a number to check: "))
print(f"{number} is {'a' if is_strong(number) else 'not a'} strong number.")

strong_numbers = [n for n in range(1, 100001) if is_strong(n)]
print(f"Strong numbers up to 100000: {strong_numbers}")
