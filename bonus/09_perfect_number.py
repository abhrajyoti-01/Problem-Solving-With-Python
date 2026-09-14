def is_perfect(number):
    if number < 2:
        return False
    divisor_sum, divisor = 1, 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor
            if number // divisor != divisor:
                divisor_sum += number // divisor
        divisor += 1
    return divisor_sum == number


number = int(input("Enter a number to check: "))
print(f"{number} is {'a perfect' if is_perfect(number) else 'not a perfect'} number.")

limit = int(input("Enter an upper limit to list all perfect numbers: "))
print(f"Perfect numbers up to {limit}: {[n for n in range(2, limit + 1) if is_perfect(n)]}")
