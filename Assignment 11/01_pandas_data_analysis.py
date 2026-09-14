import pandas as pd

data_frame = pd.read_csv("data/student_marks.csv")

print("Column headers:")
print(list(data_frame.columns))
print(f"\nDataset shape: {data_frame.shape}")
print("\nSummary:")
print(data_frame.describe(include="all"))

cleaned_frame = data_frame.copy()
for column, filler in (("Marks", "mean"), ("Attendance", "median")):
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")
    cleaned_frame[column] = cleaned_frame[column].fillna(getattr(cleaned_frame[column], filler)())

print("\nData after fillna():")
print(cleaned_frame)

print("\nData after dropna():")
print(data_frame.dropna())

print("\nRows with marks > 75:")
print(cleaned_frame[cleaned_frame["Marks"] > 75])

print("\nGrouped summary by section:")
print(cleaned_frame.groupby("Section").agg(
    average_marks=("Marks", "mean"),
    highest_marks=("Marks", "max"),
    average_attendance=("Attendance", "mean"),
))
