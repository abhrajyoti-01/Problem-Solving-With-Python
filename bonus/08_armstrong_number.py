def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digit**len(digits) for digit in digits) == number


number = int(input("Enter a number to check: "))
print(f"{number} is {'an' if is_armstrong(number) else 'not an'} Armstrong number.")

limit = int(input("Enter an upper limit to list all Armstrong numbers: "))
print(f"Armstrong numbers up to {limit}: {[n for n in range(1, limit + 1) if is_armstrong(n)]}")
