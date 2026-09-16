skip_number = 7

print("Continue statement:")
for number in range(1, 11):
    if number == skip_number:
        continue
    print(number, end=" ")
print()
