numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers:
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
else:
    print("You entered an empty list.")
