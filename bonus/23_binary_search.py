numbers = sorted(int(x) for x in input("Enter sorted list elements separated by space: ").split())
target = int(input("Enter the element to search: "))

low, high = 0, len(numbers) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print(f"{target} found at position {mid + 1}.")
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"{target} is not present in the list.")
