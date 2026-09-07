rows = int(input("Enter the number of rows: "))
for row in range(1, rows + 1):
    for _ in range(row):
        print("*", end=" ")
    print()
