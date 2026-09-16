import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("Element-wise operations")
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
