numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
other_numbers = {4, 5, 6, 7}

print(f"Original set from duplicates: {unique_numbers}")

unique_numbers.add(8)
unique_numbers.remove(1)
print(f"After add and remove: {unique_numbers}")

print(f"Union: {unique_numbers.union(other_numbers)}")
print(f"Intersection: {unique_numbers.intersection(other_numbers)}")
print(f"Difference: {unique_numbers.difference(other_numbers)}")

divisible_by_three_squares = {value * value for value in range(1, 11) if value % 3 == 0}
print(f"Squares of numbers divisible by 3: {divisible_by_three_squares}")
