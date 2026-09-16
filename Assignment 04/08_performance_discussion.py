def selection_sort(values):
    items, comparisons, swaps = values[:], 0, 0
    for current_index in range(len(items)):
        min_index = current_index
        for next_index in range(current_index + 1, len(items)):
            comparisons += 1
            if items[next_index] < items[min_index]:
                min_index = next_index
        if min_index != current_index:
            items[current_index], items[min_index] = items[min_index], items[current_index]
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
_, selection_comparisons, selection_swaps = selection_sort(values)
_, bubble_comparisons, bubble_swaps = bubble_sort(values)

print(f"Sorting a list of {len(values)} elements:")
print(f"Selection sort: {selection_comparisons} comparisons, {selection_swaps} swaps")
print(f"Bubble sort: {bubble_comparisons} comparisons, {bubble_swaps} swaps")
