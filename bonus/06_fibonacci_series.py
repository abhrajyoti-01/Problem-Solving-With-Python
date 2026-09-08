def fibonacci_series(count):
    series = []
    current, next_value = 0, 1
    for _ in range(count):
        series.append(current)
        current, next_value = next_value, current + next_value
    return series


count = int(input("How many Fibonacci numbers do you want? "))
print(f"First {count} Fibonacci numbers: {fibonacci_series(count)}")
