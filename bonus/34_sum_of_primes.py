def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


limit = int(input("Enter an upper limit: "))
primes = [n for n in range(2, limit + 1) if is_prime(n)]
print(f"Prime numbers up to {limit}: {primes}")
print(f"Count of primes: {len(primes)}")
print(f"Sum of primes up to {limit}: {sum(primes)}")
