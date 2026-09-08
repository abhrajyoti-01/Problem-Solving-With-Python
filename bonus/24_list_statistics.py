numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if not numbers:
    print("You entered an empty list.")
else:
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
