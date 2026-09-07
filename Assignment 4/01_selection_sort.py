def selection_sort(values):
    items = values[:]
    comparison_count = 0
    swap_count = 0

    for current_index in range(len(items)):
        min_index = current_index
        for next_index in range(current_index + 1, len(items)):
            comparison_count += 1
            if items[next_index] < items[min_index]:
                min_index = next_index

        print(
            f"Pass {current_index + 1}: selected {items[min_index]} "
            f"from index {min_index}"
        )

        if min_index != current_index:
            items[current_index], items[min_index] = items[min_index], items[current_index]
            swap_count += 1
            print(f"Swapped -> {items}")
        else:
            print(f"No swap needed -> {items}")

    return items, comparison_count, swap_count


values = [64, 25, 12, 22, 31]
sorted_values, comparison_count, swap_count = selection_sort(values)
print(f"Sorted list: {sorted_values}")
print(f"Comparisons: {comparison_count}")
print(f"Swaps: {swap_count}")
