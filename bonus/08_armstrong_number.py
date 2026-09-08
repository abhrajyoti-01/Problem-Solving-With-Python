def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return sum(digit**power for digit in digits) == number


number = int(input("Enter a number to check: "))
print(f"{number} is {'an' if is_armstrong(number) else 'not an'} Armstrong number.")

limit = int(input("Enter an upper limit to list all Armstrong numbers: "))
armstrong_numbers = [n for n in range(1, limit + 1) if is_armstrong(n)]
print(f"Armstrong numbers up to {limit}: {armstrong_numbers}")
