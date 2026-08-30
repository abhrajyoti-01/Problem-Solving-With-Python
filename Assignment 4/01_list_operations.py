numbers = list(range(1, 11))
print(f"Original list: {numbers}")

numbers.append(11)
numbers.insert(0, 0)
print(f"After append and insert: {numbers}")

numbers[3] = 99
numbers.remove(8)
del numbers[-1]
print(f"After update and deletion: {numbers}")

sorted_numbers = sorted(numbers)
reversed_numbers = list(reversed(sorted_numbers))
print(f"Sorted list: {sorted_numbers}")
print(f"Reversed sorted list: {reversed_numbers}")

print(f"First 5 elements: {numbers[:5]}")
print(f"Every second element: {numbers[::2]}")

even_squares = [value * value for value in numbers if value % 2 == 0]
print(f"Squares of even numbers: {even_squares}")
