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

figure, axes = plt.subplots(figsize=(8, 6))
axes.bar(mean_marks.index, mean_marks.values, color=["#5B8FF9", "#61DDAA", "#F6BD16"])
axes.set(title="Bar Plot", xlabel="Category", ylabel="Average Marks")

figure.tight_layout()
figure.savefig("output/03_bar_plot.png", dpi=200)
plt.close(figure)

print("Bar plot saved to output/03_bar_plot.png")
