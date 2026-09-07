def factorial(number):
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


number = 6
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} is {factorial(number)}")
