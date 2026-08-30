mixed_tuple = (1, "Python", 3.14)
single_element_tuple = (5,)
nested_tuple = (1, (2, 3), 4)
values = (10, 20, 10, 30)

print(f"Mixed tuple: {mixed_tuple}")
print(f"Single-element tuple: {single_element_tuple}")
print(f"Nested tuple: {nested_tuple}")

first_value, second_value, third_value = mixed_tuple
print(f"Tuple unpacking: {first_value}, {second_value}, {third_value}")
print(f"Value at index 1 in nested tuple: {nested_tuple[1]}")
print(f"Count of 10: {values.count(10)}")
print(f"Index of 30: {values.index(30)}")
