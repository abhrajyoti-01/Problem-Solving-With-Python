import pandas as pd

SUBJECT_COLUMNS = ["Math", "Science", "English", "History"]

data_frame = pd.read_csv("data/student_records.csv")

cleaned_frame = data_frame.copy()
for column in SUBJECT_COLUMNS + ["Attendance"]:
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")

print("Missing values before handling:")
print(data_frame.isna().sum())

for column in SUBJECT_COLUMNS:
    cleaned_frame[column] = cleaned_frame[column].fillna(cleaned_frame[column].mean())
cleaned_frame["Attendance"] = cleaned_frame["Attendance"].fillna(cleaned_frame["Attendance"].median())

print("\nMissing values after handling:")
print(cleaned_frame.isna().sum())
