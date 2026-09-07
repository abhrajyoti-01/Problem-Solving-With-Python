import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


SUBJECT_COLUMNS = ["Math", "Science", "English", "History"]


sns.set_theme(style="whitegrid")

os.makedirs("output", exist_ok=True)

data_frame = pd.read_csv("data/student_records.csv")
print("Top 5 records:")
print(data_frame.head())
print("\nBottom 5 records:")
print(data_frame.tail())

cleaned_frame = data_frame.copy()
for column in SUBJECT_COLUMNS + ["Attendance"]:
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")

for column in SUBJECT_COLUMNS:
    cleaned_frame[column] = cleaned_frame[column].fillna(cleaned_frame[column].mean())
cleaned_frame["Attendance"] = cleaned_frame["Attendance"].fillna(cleaned_frame["Attendance"].median())

cleaned_frame["Total"] = cleaned_frame[SUBJECT_COLUMNS].sum(axis=1)
cleaned_frame["Average"] = cleaned_frame[SUBJECT_COLUMNS].mean(axis=1)
cleaned_frame["Result"] = cleaned_frame[SUBJECT_COLUMNS].ge(40).all(axis=1).map(
    {True: "Pass", False: "Fail"}
)

print("\nAverage score per subject:")
print(cleaned_frame[SUBJECT_COLUMNS].mean())

print("\nTop 5 students by total score:")
top_students = cleaned_frame.nlargest(5, "Total")[["StudentID", "Name", "Total"]]
print(top_students)

print("\nGender-wise average marks:")
gender_analysis = cleaned_frame.groupby("Gender")[SUBJECT_COLUMNS].mean()
print(gender_analysis)

trend_student = cleaned_frame.loc[cleaned_frame["Total"].idxmax(), ["Name"] + SUBJECT_COLUMNS].copy()
student_name = trend_student["Name"]

figure, axes = plt.subplots(2, 2, figsize=(14, 10))

subject_averages = cleaned_frame[SUBJECT_COLUMNS].mean()
axes[0, 0].bar(subject_averages.index, subject_averages.values, color="tab:blue")
axes[0, 0].set_title("Average Marks per Subject")
axes[0, 0].set_ylabel("Average Marks")

subject_scores = cleaned_frame.melt(
    id_vars=["StudentID", "Name"],
    value_vars=SUBJECT_COLUMNS,
    var_name="Subject",
    value_name="Score",
)
sns.boxplot(data=subject_scores, x="Subject", y="Score", ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Subject Score Distribution")

axes[1, 0].hist(cleaned_frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes[1, 0].set_title("Attendance Distribution")
axes[1, 0].set_xlabel("Attendance Percentage")
axes[1, 0].set_ylabel("Frequency")

axes[1, 1].plot(
    SUBJECT_COLUMNS,
    [trend_student[column] for column in SUBJECT_COLUMNS],
    marker="o",
    color="tab:green",
)
axes[1, 1].set_title(f"Academic Trend for {student_name}")
axes[1, 1].set_ylabel("Marks")

figure.tight_layout()
figure.savefig("output/student_academic_analysis.png", dpi=200)
plt.close(figure)

print("\nResult counts:")
print(cleaned_frame["Result"].value_counts())
print("\nPlot saved to output/student_academic_analysis.png")
