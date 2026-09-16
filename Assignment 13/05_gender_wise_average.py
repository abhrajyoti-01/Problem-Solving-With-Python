import pandas as pd

SUBJECT_COLUMNS = ["Math", "Science", "English", "History"]

data_frame = pd.read_csv("data/student_records.csv")
for column in SUBJECT_COLUMNS:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")
    data_frame[column] = data_frame[column].fillna(data_frame[column].mean())

print("Gender-wise average marks:")
print(data_frame.groupby("Gender")[SUBJECT_COLUMNS].mean())
