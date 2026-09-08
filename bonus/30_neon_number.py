def is_neon(number):
    square = number * number
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == number


number = int(input("Enter a number to check: "))
print(f"{number} is {'a' if is_neon(number) else 'not a'} neon number.")

neon_numbers = [n for n in range(0, 10001) if is_neon(n)]
print(f"Neon numbers up to 10000: {neon_numbers}")
