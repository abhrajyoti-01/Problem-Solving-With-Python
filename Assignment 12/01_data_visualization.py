import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

frame = pd.read_csv("data/visualization_data.csv")
figure, axes = plt.subplots(2, 3, figsize=(16, 10))

axes[0, 0].scatter(frame["StudyHours"], frame["Marks"], color="tab:blue", label="Hours vs Marks")
axes[0, 0].set(title="Scatter Plot", xlabel="Study Hours", ylabel="Marks")
axes[0, 0].legend()

axes[0, 1].plot(frame["Month"], frame["Marks"], color="tab:green", marker="o", label="Marks Trend")
axes[0, 1].set(title="Line Plot", xlabel="Month", ylabel="Marks")
axes[0, 1].legend()

mean_marks = frame.groupby("Category")["Marks"].mean()
axes[0, 2].bar(mean_marks.index, mean_marks.values, color=["#5B8FF9", "#61DDAA", "#F6BD16"])
axes[0, 2].set(title="Bar Plot", xlabel="Category", ylabel="Average Marks")

axes[1, 0].hist(frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes[1, 0].set(title="Histogram", xlabel="Attendance", ylabel="Frequency")

sns.boxplot(data=frame, y="Marks", x="Category", ax=axes[1, 1], palette="Set2")
axes[1, 1].set(title="Box Plot", xlabel="Category", ylabel="Marks")

axes[1, 2].plot(frame["Month"], frame["Attendance"], color="tab:red", marker="s", label="Attendance")
axes[1, 2].set(title="Styled Subplot", xlabel="Month", ylabel="Attendance")
axes[1, 2].legend()

figure.tight_layout()
figure.savefig("output/assignment_13_plots.png", dpi=200)
plt.close(figure)

pair_plot = sns.pairplot(frame[["StudyHours", "Marks", "Attendance"]])
pair_plot.fig.suptitle("Pair Plot", y=1.02)
pair_plot.savefig("output/assignment_13_pairplot.png", dpi=200)
plt.close(pair_plot.fig)

print("Plots saved in the output folder.")
