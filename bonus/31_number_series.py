n = int(input("How many terms of the series to print? "))

# Series: 1 + 2 + 3 + ... + n = n*(n+1)/2
series_sum = n * (n + 1) // 2
print(f"Sum of first {n} natural numbers: {series_sum}")

# Series: 1^2 + 2^2 + ... + n^2
square_sum = sum(i * i for i in range(1, n + 1))
print(f"Sum of squares of first {n} natural numbers: {square_sum}")

# Series: 1/1 + 1/2 + 1/3 + ... + 1/n
harmonic = sum(1 / i for i in range(1, n + 1))
print(f"Harmonic series sum up to {n} terms: {harmonic:.4f}")

# Series: 1! + 2! + ... + n!
factorial_sum = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    factorial_sum += factorial
print(f"Sum of factorials 1! + 2! + ... + {n}!: {factorial_sum}")
