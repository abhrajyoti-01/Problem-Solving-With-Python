def fibonacci(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return fibonacci(position - 1) + fibonacci(position - 2)


position = int(input("Enter the Fibonacci position: "))
if position < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"Fibonacci value at position {position} is {fibonacci(position)}")
