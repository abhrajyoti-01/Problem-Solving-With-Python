import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

os.makedirs("output", exist_ok=True)

data_frame = pd.read_csv("data/visualization_data.csv")

figure, axes = plt.subplots(2, 3, figsize=(16, 10))

axes[0, 0].scatter(
    data_frame["StudyHours"],
    data_frame["Marks"],
    color="tab:blue",
    label="Hours vs Marks",
)
axes[0, 0].set_title("Scatter Plot")
axes[0, 0].set_xlabel("Study Hours")
axes[0, 0].set_ylabel("Marks")
axes[0, 0].legend()

axes[0, 1].plot(
    data_frame["Month"],
    data_frame["Marks"],
    color="tab:green",
    marker="o",
    label="Marks Trend",
)
axes[0, 1].set_title("Line Plot")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Marks")
axes[0, 1].legend()

mean_marks = data_frame.groupby("Category")["Marks"].mean()
axes[0, 2].bar(mean_marks.index, mean_marks.values, color=["#5B8FF9", "#61DDAA", "#F6BD16"])
axes[0, 2].set_title("Bar Plot")
axes[0, 2].set_xlabel("Category")
axes[0, 2].set_ylabel("Average Marks")

axes[1, 0].hist(data_frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes[1, 0].set_title("Histogram")
axes[1, 0].set_xlabel("Attendance")
axes[1, 0].set_ylabel("Frequency")

sns.boxplot(data=data_frame, y="Marks", x="Category", ax=axes[1, 1], palette="Set2")
axes[1, 1].set_title("Box Plot")
axes[1, 1].set_xlabel("Category")
axes[1, 1].set_ylabel("Marks")

axes[1, 2].plot(
    data_frame["Month"],
    data_frame["Attendance"],
    color="tab:red",
    marker="s",
    label="Attendance",
)
axes[1, 2].set_title("Styled Subplot")
axes[1, 2].set_xlabel("Month")
axes[1, 2].set_ylabel("Attendance")
axes[1, 2].legend()

figure.tight_layout()
figure.savefig("output/assignment_13_plots.png", dpi=200)
plt.close(figure)

pair_plot = sns.pairplot(data_frame[["StudyHours", "Marks", "Attendance"]])
pair_plot.fig.suptitle("Pair Plot", y=1.02)
pair_plot.savefig("output/assignment_13_pairplot.png", dpi=200)
plt.close(pair_plot.fig)

print("Plots saved in the output folder.")
