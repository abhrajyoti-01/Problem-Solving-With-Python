number = int(input("Enter a number to factorize: "))

original, factors, divisor = number, [], 2
while divisor * divisor <= number:
    while number % divisor == 0:
        factors.append(divisor)
        number //= divisor
    divisor += 1
if number > 1:
    factors.append(number)

print(f"{original} is a prime number." if len(factors) <= 1 else f"Prime factorization of {original}: {' x '.join(str(f) for f in factors)}")
