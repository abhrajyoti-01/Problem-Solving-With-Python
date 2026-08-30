skip_number = int(input("Enter the number to skip: "))

for number in range(1, 11):
    if number == skip_number:
        continue
    print(number, end=" ")
print()
