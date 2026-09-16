import pandas as pd

data_frame = pd.read_csv("data/student_records.csv")

print("Top 5 records:")
print(data_frame.head())
print("\nBottom 5 records:")
print(data_frame.tail())
