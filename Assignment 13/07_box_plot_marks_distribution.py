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

subject_scores = data_frame.melt(id_vars=["StudentID", "Name"], value_vars=SUBJECT_COLUMNS, var_name="Subject", value_name="Score")
figure, axes = plt.subplots(figsize=(8, 6))
sns.boxplot(data=subject_scores, x="Subject", y="Score", hue="Subject", ax=axes, palette="Set2", legend=False)
axes.set(title="Subject Score Distribution", xlabel="Subject", ylabel="Marks")

figure.tight_layout()
figure.savefig("output/07_box_plot_marks_distribution.png", dpi=200)
plt.close(figure)

print("Box plot saved to output/07_box_plot_marks_distribution.png")
