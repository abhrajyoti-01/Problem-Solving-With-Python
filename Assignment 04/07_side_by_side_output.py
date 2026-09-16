def selection_sort(values):
    items = values[:]
    for current_index in range(len(items)):
        min_index = current_index
        for next_index in range(current_index + 1, len(items)):
            if items[next_index] < items[min_index]:
                min_index = next_index
        items[current_index], items[min_index] = items[min_index], items[current_index]
    return items


def bubble_sort(values):
    items = values[:]
    for pass_number in range(len(items) - 1):
        for index in range(len(items) - 1 - pass_number):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items


values = [64, 25, 12, 22, 31]
selection_sorted = selection_sort(values)
bubble_sorted = bubble_sort(values)

print(f"{'Selection Sort':<20}{'Bubble Sort':<20}")
print("-" * 40)
for selection_value, bubble_value in zip(selection_sorted, bubble_sorted):
    print(f"{selection_value:<20}{bubble_value:<20}")
