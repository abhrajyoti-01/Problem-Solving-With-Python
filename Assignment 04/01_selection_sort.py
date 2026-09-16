values = [64, 25, 12, 22, 31]
items = values[:]

for current_index in range(len(items)):
    min_index = current_index
    for next_index in range(current_index + 1, len(items)):
        if items[next_index] < items[min_index]:
            min_index = next_index
    items[current_index], items[min_index] = items[min_index], items[current_index]

print(f"Original list: {values}")
print(f"Sorted list: {items}")
