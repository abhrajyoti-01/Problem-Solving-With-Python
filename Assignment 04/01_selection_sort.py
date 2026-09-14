values = [64, 25, 12, 22, 31]
items = values[:]
comparison_count = swap_count = 0

for current_index in range(len(items)):
    min_index = current_index
    for next_index in range(current_index + 1, len(items)):
        comparison_count += 1
        if items[next_index] < items[min_index]:
            min_index = next_index
    print(f"Pass {current_index + 1}: selected {items[min_index]} from index {min_index}")
    if min_index != current_index:
        items[current_index], items[min_index] = items[min_index], items[current_index]
        swap_count += 1
        print(f"Swapped -> {items}")
    else:
        print(f"No swap needed -> {items}")

print(f"Sorted list: {items}")
print(f"Comparisons: {comparison_count}")
print(f"Swaps: {swap_count}")
