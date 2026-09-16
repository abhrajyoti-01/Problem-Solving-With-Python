stop_number = 5

print("Break statement:")
for number in range(1, 11):
    if number == stop_number:
        print("Loop stopped.")
        break
    print(number, end=" ")
print()
