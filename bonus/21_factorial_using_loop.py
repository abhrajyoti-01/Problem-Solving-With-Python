number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    print(f"Factorial of {number} is {factorial}")
