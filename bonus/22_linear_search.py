numbers = list(map(int, input("Enter the list elements separated by space: ").split()))
target = int(input("Enter the element to search: "))

found = False
for index, value in enumerate(numbers):
    if value == target:
        print(f"{target} found at position {index + 1}.")
        found = True
        break

if not found:
    print(f"{target} is not present in the list.")
