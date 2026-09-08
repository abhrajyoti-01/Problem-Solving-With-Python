def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


number = int(input("Enter a number to check: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

limit = int(input("Enter an upper limit to list all primes: "))
primes = [n for n in range(2, limit + 1) if is_prime(n)]
print(f"Prime numbers up to {limit}: {primes}")
