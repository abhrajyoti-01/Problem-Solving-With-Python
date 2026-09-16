import pandas as pd

SUBJECT_COLUMNS = ["Math", "Science", "English", "History"]

data_frame = pd.read_csv("data/student_records.csv")
for column in SUBJECT_COLUMNS:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")
    data_frame[column] = data_frame[column].fillna(data_frame[column].mean())

data_frame["Total"] = data_frame[SUBJECT_COLUMNS].sum(axis=1)
data_frame["Result"] = data_frame[SUBJECT_COLUMNS].ge(40).all(axis=1).map({True: "Pass", False: "Fail"})

print(data_frame[["StudentID", "Name", "Total", "Result"]])
print("\nResult counts:")
print(data_frame["Result"].value_counts())
