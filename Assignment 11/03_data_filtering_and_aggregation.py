import pandas as pd

data_frame = pd.read_csv("data/student_marks.csv")

cleaned_frame = data_frame.copy()
for column, filler in (("Marks", "mean"), ("Attendance", "median")):
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")
    cleaned_frame[column] = cleaned_frame[column].fillna(getattr(cleaned_frame[column], filler)())

print("Rows with marks > 75:")
print(cleaned_frame[cleaned_frame["Marks"] > 75])

print("\nGrouped summary by section:")
print(cleaned_frame.groupby("Section").agg(
    average_marks=("Marks", "mean"),
    highest_marks=("Marks", "max"),
    average_attendance=("Attendance", "mean"),
))
