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
for column in SUBJECT_COLUMNS:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")
    data_frame[column] = data_frame[column].fillna(data_frame[column].mean())

data_frame["Total"] = data_frame[SUBJECT_COLUMNS].sum(axis=1)
trend_student = data_frame.loc[data_frame["Total"].idxmax(), ["Name"] + SUBJECT_COLUMNS]

figure, axes = plt.subplots(figsize=(8, 6))
axes.plot(SUBJECT_COLUMNS, [trend_student[column] for column in SUBJECT_COLUMNS], marker="o", color="tab:green")
axes.set(title=f"Academic Trend for {trend_student['Name']}", xlabel="Subject", ylabel="Marks")

figure.tight_layout()
figure.savefig("output/09_line_plot_student_trend.png", dpi=200)
plt.close(figure)

print(f"Line plot saved to output/09_line_plot_student_trend.png")
