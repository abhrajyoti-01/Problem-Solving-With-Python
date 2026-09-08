def read_matrix(name):
    rows = int(input(f"Enter number of rows in matrix {name}: "))
    cols = int(input(f"Enter number of columns in matrix {name}: "))
    print(f"Enter {rows * cols} elements of matrix {name}, row by row:")
    return [list(map(int, input().split())) for _ in range(rows)]


def add_matrices(a, b):
    rows, cols = len(a), len(a[0])
    return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]


def subtract_matrices(a, b):
    rows, cols = len(a), len(a[0])
    return [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(f"{value:>4}" for value in row))


a = read_matrix("A")
b = read_matrix("B")

if len(a) != len(b) or len(a[0]) != len(b[0]):
    print("Matrices must have the same dimensions for addition/subtraction.")
else:
    print("Matrix A:")
    print_matrix(a)
    print("Matrix B:")
    print_matrix(b)
    print("A + B:")
    print_matrix(add_matrices(a, b))
    print("A - B:")
    print_matrix(subtract_matrices(a, b))
