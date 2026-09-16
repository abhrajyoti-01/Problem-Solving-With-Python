values = [int(value) for value in input("Enter the numbers to sort, separated by spaces: ").split()]
items = values[:]

for current_index in range(len(items)):
    min_index = current_index
    for next_index in range(current_index + 1, len(items)):
        if items[next_index] < items[min_index]:
            min_index = next_index
    print(f"Pass {current_index + 1}: selected {items[min_index]} from index {min_index}")
    if min_index != current_index:
        items[current_index], items[min_index] = items[min_index], items[current_index]
        print(f"Swapped -> {items}")
    else:
        print(f"No swap needed -> {items}")

print(f"Sorted list: {items}")
