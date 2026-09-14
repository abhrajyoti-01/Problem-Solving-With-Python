def is_prime(number):
    if number < 2 or (number > 2 and number % 2 == 0):
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


number = int(input("Enter a number to check: "))
print(f"{number} is {'a prime' if is_prime(number) else 'not a prime'} number.")

limit = int(input("Enter an upper limit to list all primes: "))
print(f"Prime numbers up to {limit}: {[n for n in range(2, limit + 1) if is_prime(n)]}")
