n = int(input("How many terms of the series to print? "))

print(f"Sum of first {n} natural numbers: {n * (n + 1) // 2}")
print(f"Sum of squares of first {n} natural numbers: {sum(i * i for i in range(1, n + 1))}")
print(f"Harmonic series sum up to {n} terms: {sum(1 / i for i in range(1, n + 1)):.4f}")

factorial, factorial_sum = 1, 0
for i in range(1, n + 1):
    factorial *= i
    factorial_sum += factorial
print(f"Sum of factorials 1! + 2! + ... + {n}!: {factorial_sum}")
