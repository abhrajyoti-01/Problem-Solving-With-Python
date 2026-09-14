def read_matrix(name):
    rows = int(input(f"Enter number of rows in matrix {name}: "))
    cols = int(input(f"Enter number of columns in matrix {name}: "))
    print(f"Enter {rows * cols} elements of matrix {name}, row by row:")
    return [list(map(int, input().split())) for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(f"{value:>4}" for value in row))


a, b = read_matrix("A"), read_matrix("B")

if (len(a), len(a[0])) != (len(b), len(b[0])):
    print("Matrices must have the same dimensions for addition/subtraction.")
else:
    print("Matrix A:")
    print_matrix(a)
    print("Matrix B:")
    print_matrix(b)
    print("A + B:")
    print_matrix([[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)])
    print("A - B:")
    print_matrix([[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)])
