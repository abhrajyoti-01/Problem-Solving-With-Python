import pandas as pd

data_frame = pd.read_csv("data/student_marks.csv")

print("Column headers:")
print(list(data_frame.columns))
print(f"\nDataset shape: {data_frame.shape}")
print("\nSummary:")
print(data_frame.describe(include="all"))
