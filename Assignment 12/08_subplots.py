import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

frame = pd.read_csv("data/visualization_data.csv")

mean_marks = frame.groupby("Category")["Marks"].mean()
figure, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(frame["Month"], frame["Marks"], color="tab:green", marker="o")
axes[0, 0].set(title="Line Plot", xlabel="Month", ylabel="Marks")

axes[0, 1].bar(mean_marks.index, mean_marks.values, color="tab:blue")
axes[0, 1].set(title="Bar Plot", xlabel="Category", ylabel="Average Marks")

axes[1, 0].scatter(frame["StudyHours"], frame["Marks"], color="tab:purple")
axes[1, 0].set(title="Scatter Plot", xlabel="Study Hours", ylabel="Marks")

axes[1, 1].hist(frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes[1, 1].set(title="Histogram", xlabel="Attendance", ylabel="Frequency")

figure.tight_layout()
figure.savefig("output/08_subplots.png", dpi=200)
plt.close(figure)

print("Subplots saved to output/08_subplots.png")
