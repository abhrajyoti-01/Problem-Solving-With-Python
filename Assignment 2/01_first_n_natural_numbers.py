count = int(input("Enter the value of N: "))
if count <= 0:
    print("Please enter a positive integer.")
else:
    print(f"First {count} natural numbers:")
    for number in range(1, count + 1):
        print(number, end=" ")
    print()
