stop_number = int(input("Enter the number at which the loop should stop: "))
skip_number = int(input("Enter the number to skip: "))

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
