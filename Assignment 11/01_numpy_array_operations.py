import numpy as np


array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:")
print(array_1d)
print(f"Dimensions: {array_1d.ndim}, Shape: {array_1d.shape}, Dtype: {array_1d.dtype}")

print("\n2D Array:")
print(array_2d)
print(f"Dimensions: {array_2d.ndim}, Shape: {array_2d.shape}, Dtype: {array_2d.dtype}")

print("\n3D Array:")
print(array_3d)
print(f"Dimensions: {array_3d.ndim}, Shape: {array_3d.shape}, Dtype: {array_3d.dtype}")

print("\nElement-wise operations")
print(f"array_1d + 10 = {array_1d + 10}")
print(f"array_1d * 2 = {array_1d * 2}")

print("\nStatistics")
print(f"Sum: {array_1d.sum()}")
print(f"Mean: {array_1d.mean()}")
print(f"Max: {array_1d.max()}")
print(f"Min: {array_1d.min()}")
print(f"Standard deviation: {array_1d.std()}")

print("\nSlicing")
print(f"First row of 2D array: {array_2d[0]}")
print(f"Second column of 2D array: {array_2d[:, 1]}")
print(f"Specific element array_2d[1, 2]: {array_2d[1, 2]}")

reshaped_array = np.arange(1, 13).reshape(3, 4)
print("\nReshaped array (3x4):")
print(reshaped_array)
print(f"Flattened with ravel(): {reshaped_array.ravel()}")

print("\nBroadcasting")
print(reshaped_array + 5)
print(reshaped_array + np.array([1, 2, 3, 4]))

math_array = np.array([1, 4, 9, 16], dtype=float)
print("\nMathematical functions")
print(f"sqrt: {np.sqrt(math_array)}")
print(f"exp: {np.exp(np.array([1, 2, 3]))}")
print(f"log: {np.log(math_array)}")

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print("\nMatrix multiplication using np.dot():")
print(np.dot(matrix_a, matrix_b))
