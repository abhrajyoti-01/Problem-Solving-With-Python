values = [64, 25, 12, 22, 31]
items = values[:]

for pass_number in range(len(items) - 1):
    for index in range(len(items) - 1 - pass_number):
        if items[index] > items[index + 1]:
            items[index], items[index + 1] = items[index + 1], items[index]

print(f"Original list: {values}")
print(f"Sorted list: {items}")
