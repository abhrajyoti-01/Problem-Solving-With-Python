import pandas as pd


data_frame = pd.read_csv("data/student_marks.csv")

print("Column headers:")
print(list(data_frame.columns))
print(f"\nDataset shape: {data_frame.shape}")
print("\nSummary:")
print(data_frame.describe(include="all"))

cleaned_frame = data_frame.copy()
cleaned_frame["Marks"] = pd.to_numeric(cleaned_frame["Marks"], errors="coerce")
cleaned_frame["Attendance"] = pd.to_numeric(cleaned_frame["Attendance"], errors="coerce")
cleaned_frame["Marks"] = cleaned_frame["Marks"].fillna(cleaned_frame["Marks"].mean())
cleaned_frame["Attendance"] = cleaned_frame["Attendance"].fillna(cleaned_frame["Attendance"].median())

print("\nData after fillna():")
print(cleaned_frame)

dropped_frame = data_frame.dropna()
print("\nData after dropna():")
print(dropped_frame)

filtered_frame = cleaned_frame[cleaned_frame["Marks"] > 75]
print("\nRows with marks > 75:")
print(filtered_frame)

grouped_summary = cleaned_frame.groupby("Section").agg(
    average_marks=("Marks", "mean"),
    highest_marks=("Marks", "max"),
    average_attendance=("Attendance", "mean"),
)
print("\nGrouped summary by section:")
print(grouped_summary)
