def fibonacci(position):
    return position if position < 2 else fibonacci(position - 1) + fibonacci(position - 2)


position = 7
print("Please enter a non-negative integer." if position < 0 else f"Fibonacci value at position {position} is {fibonacci(position)}")
