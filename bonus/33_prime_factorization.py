number = int(input("Enter a number to factorize: "))

original = number
factors = []
divisor = 2
while divisor * divisor <= number:
    while number % divisor == 0:
        factors.append(divisor)
        number //= divisor
    divisor += 1
if number > 1:
    factors.append(number)

if len(factors) <= 1:
    print(f"{original} is a prime number.")
else:
    print(f"Prime factorization of {original}: {' x '.join(str(f) for f in factors)}")
