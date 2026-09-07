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

        if min_index != current_index:
            items[current_index], items[min_index] = items[min_index], items[current_index]
            swap_count += 1

    return items, comparison_count, swap_count


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
        if not swapped:
            break

    return items, comparison_count, swap_count


raw_values = input("Enter numbers separated by spaces: ").split()
values = [int(value) for value in raw_values]

selection_result = selection_sort(values)
bubble_result = bubble_sort(values)

print(f"{'Algorithm':<18}{'Sorted Output':<24}{'Comparisons':<14}{'Swaps':<10}")
print("-" * 66)
print(
    f"{'Selection Sort':<18}{str(selection_result[0]):<24}"
    f"{selection_result[1]:<14}{selection_result[2]:<10}"
)
print(
    f"{'Bubble Sort':<18}{str(bubble_result[0]):<24}"
    f"{bubble_result[1]:<14}{bubble_result[2]:<10}"
)
