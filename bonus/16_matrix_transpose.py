def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


def print_matrix(matrix):
    for row in matrix:
        print("\t".join(f"{value:>4}" for value in row))


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print(f"Enter {rows * cols} elements, row by row:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

print("Original matrix:")
print_matrix(matrix)
print("Transpose:")
print_matrix(transpose(matrix))
