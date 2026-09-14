count = int(input("How many numbers? "))
numbers = [int(input(f"Number {i + 1}: ")) for i in range(count)]

print(f"Numbers: {numbers}")
print(f"Sum of even numbers: {sum(n for n in numbers if n % 2 == 0)}")
print(f"Sum of odd numbers: {sum(n for n in numbers if n % 2 != 0)}")
print(f"Even count: {sum(1 for n in numbers if n % 2 == 0)}")
print(f"Odd count: {sum(1 for n in numbers if n % 2 != 0)}")
