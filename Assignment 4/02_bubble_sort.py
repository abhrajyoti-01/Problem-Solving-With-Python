def bubble_sort(values):
    items = values[:]
    comparison_count = 0
    swap_count = 0

    for pass_number in range(len(items) - 1):
        swapped = False
        for current_index in range(len(items) - 1 - pass_number):
            comparison_count += 1
            if items[current_index] > items[current_index + 1]:
                items[current_index], items[current_index + 1] = (
                    items[current_index + 1],
                    items[current_index],
                )
                swap_count += 1
                swapped = True
        print(f"After pass {pass_number + 1}: {items}")
        if not swapped:
            break

    return items, comparison_count, swap_count


values = [64, 25, 12, 22, 31]
sorted_values, comparison_count, swap_count = bubble_sort(values)
print(f"Sorted list: {sorted_values}")
print(f"Comparisons: {comparison_count}")
print(f"Swaps: {swap_count}")
