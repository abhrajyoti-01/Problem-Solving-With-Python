def selection_sort(values):
    items, comparisons, swaps = values[:], 0, 0
    for index in range(len(items)):
        min_index = index
        for next_index in range(index + 1, len(items)):
            comparisons += 1
            if items[next_index] < items[min_index]:
                min_index = next_index
        if min_index != index:
            items[index], items[min_index] = items[min_index], items[index]
            swaps += 1
    return items, comparisons, swaps


def bubble_sort(values):
    items, comparisons, swaps = values[:], 0, 0
    for pass_number in range(len(items) - 1):
        swapped = False
        for index in range(len(items) - 1 - pass_number):
            comparisons += 1
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return items, comparisons, swaps


values = [64, 25, 12, 22, 31]
selection_result = selection_sort(values)
bubble_result = bubble_sort(values)

print(f"{'Algorithm':<18}{'Sorted Output':<24}{'Comparisons':<14}{'Swaps':<10}")
print("-" * 66)
print(f"{'Selection Sort':<18}{str(selection_result[0]):<24}{selection_result[1]:<14}{selection_result[2]:<10}")
print(f"{'Bubble Sort':<18}{str(bubble_result[0]):<24}{bubble_result[1]:<14}{bubble_result[2]:<10}")
