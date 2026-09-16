import pandas as pd

data_frame = pd.read_csv("data/student_marks.csv")

cleaned_frame = data_frame.copy()
for column, filler in (("Marks", "mean"), ("Attendance", "median")):
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")
    cleaned_frame[column] = cleaned_frame[column].fillna(getattr(cleaned_frame[column], filler)())

print("Data after fillna():")
print(cleaned_frame)

print("\nData after dropna():")
print(data_frame.dropna())
