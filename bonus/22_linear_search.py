numbers = list(map(int, input("Enter the list elements separated by space: ").split()))
target = int(input("Enter the element to search: "))

if target in numbers:
    print(f"{target} found at position {numbers.index(target) + 1}.")
else:
    print(f"{target} is not present in the list.")
