def is_strong(number):
    original = number
    total = 0
    while number > 0:
        digit = number % 10
        factorial = 1
        for i in range(2, digit + 1):
            factorial *= i
        total += factorial
        number //= 10
    return original == total


number = int(input("Enter a number to check: "))
print(f"{number} is {'a' if is_strong(number) else 'not a'} strong number.")

strong_numbers = [n for n in range(1, 100001) if is_strong(n)]
print(f"Strong numbers up to 100000: {strong_numbers}")
