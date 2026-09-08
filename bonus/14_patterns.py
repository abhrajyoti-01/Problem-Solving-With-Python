n = int(input("Enter the number of rows for the patterns: "))

# Right-angled triangle pattern
for i in range(1, n + 1):
    print("* " * i)

print()

# Inverted right-angled triangle pattern
for i in range(n, 0, -1):
    print("* " * i)

print()

# Pyramid pattern
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print()

# Number pyramid pattern
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))
