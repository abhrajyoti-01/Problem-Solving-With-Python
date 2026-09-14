n = int(input("Enter the number of rows: "))

print("\n1. Diamond pattern")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

print("\n2. Inverted pyramid")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

print("\n3. Number pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(i) for _ in range(i)))

print("\n4. Floyd's triangle")
value = 1
for i in range(1, n + 1):
    print(" ".join(str(value + j) for j in range(i)))
    value += i
