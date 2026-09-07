stop_number = 5
skip_number = 7

print("Break statement:")
for number in range(1, 11):
    if number == stop_number:
        print("Loop stopped.")
        break
    print(number, end=" ")
print()

print("\nContinue statement:")
for number in range(1, 11):
    if number == skip_number:
        continue
    print(number, end=" ")
print()

print("\nPass statement:")
for number in range(1, 6):
    if number == 3:
        pass
    print(number, end=" ")
print()
