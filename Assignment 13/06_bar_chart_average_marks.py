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

subject_averages = data_frame[SUBJECT_COLUMNS].mean()
figure, axes = plt.subplots(figsize=(8, 6))
axes.bar(subject_averages.index, subject_averages.values, color="tab:blue")
axes.set(title="Average Marks per Subject", xlabel="Subject", ylabel="Average Marks")

figure.tight_layout()
figure.savefig("output/06_bar_chart_average_marks.png", dpi=200)
plt.close(figure)

print("Bar chart saved to output/06_bar_chart_average_marks.png")
