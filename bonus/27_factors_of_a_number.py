number = int(input("Enter a number: "))
factors = [i for i in range(1, number + 1) if number % i == 0]
print(f"Factors of {number}: {factors}")
print(f"Number of factors: {len(factors)}")
