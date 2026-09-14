values = [64, 25, 12, 22, 31]
items = values[:]
comparison_count = swap_count = 0

for pass_number in range(len(items) - 1):
    swapped = False
    for index in range(len(items) - 1 - pass_number):
        comparison_count += 1
        if items[index] > items[index + 1]:
            items[index], items[index + 1] = items[index + 1], items[index]
            swap_count += 1
            swapped = True
    print(f"After pass {pass_number + 1}: {items}")
    if not swapped:
        break

print(f"Sorted list: {items}")
print(f"Comparisons: {comparison_count}")
print(f"Swaps: {swap_count}")
