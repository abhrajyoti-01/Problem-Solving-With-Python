import numpy as np

math_array = np.array([1, 4, 9, 16], dtype=float)
print("Mathematical functions")
print(f"sqrt: {np.sqrt(math_array)}")
print(f"exp: {np.exp(np.array([1, 2, 3]))}")
print(f"log: {np.log(math_array)}")

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("\nMatrix multiplication using np.dot():")
print(np.dot(matrix_a, matrix_b))
