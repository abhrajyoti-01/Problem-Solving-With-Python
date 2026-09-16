import numpy as np

reshaped_array = np.arange(1, 13).reshape(3, 4)
print("Reshaped array (3x4):")
print(reshaped_array)
print(f"Flattened with ravel(): {reshaped_array.ravel()}")

print("\nBroadcasting a scalar")
print(reshaped_array + 5)

print("\nBroadcasting a vector")
print(reshaped_array + np.array([1, 2, 3, 4]))
