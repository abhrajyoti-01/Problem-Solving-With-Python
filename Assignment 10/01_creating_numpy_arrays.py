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
