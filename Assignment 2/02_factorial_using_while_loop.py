number = 5
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    current = 1
    while current <= number:
        factorial *= current
        current += 1

    print(f"Factorial of {number} is {factorial}.")
