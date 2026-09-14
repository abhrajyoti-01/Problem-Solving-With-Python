def read_matrix(name):
    rows = int(input(f"Enter number of rows in matrix {name}: "))
    cols = int(input(f"Enter number of columns in matrix {name}: "))
    print(f"Enter {rows * cols} elements of matrix {name}, row by row:")
    return [list(map(int, input().split())) for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(f"{value:>6.2f}" for value in row))


def divide_matrix_by_scalar(matrix, scalar):
    if scalar == 0:
        raise ZeroDivisionError("Cannot divide a matrix by zero.")
    return [[value / scalar for value in row] for row in matrix]


a, b = read_matrix("A"), read_matrix("B")

if len(a[0]) != len(b):
    print(f"Cannot multiply: A has {len(a[0])} columns but B has {len(b)} rows.")
else:
    print("A x B:")
    print_matrix([[sum(x * y for x, y in zip(row, column)) for column in zip(*b)] for row in a])

scalar = float(input("Enter a scalar to divide matrix A by: "))
print(f"A / {scalar}:")
print_matrix(divide_matrix_by_scalar(a, scalar))
