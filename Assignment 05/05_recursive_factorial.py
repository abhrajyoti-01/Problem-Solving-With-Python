def factorial(number):
    return 1 if number in (0, 1) else number * factorial(number - 1)


number = 6
print("Factorial is not defined for negative numbers." if number < 0 else f"Factorial of {number} is {factorial(number)}")
