import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

frame = pd.read_csv("data/visualization_data.csv")

figure, axes = plt.subplots(figsize=(8, 6))
axes.scatter(frame["StudyHours"], frame["Marks"], color="tab:blue", label="Hours vs Marks")
axes.set(title="Scatter Plot", xlabel="Study Hours", ylabel="Marks")
axes.legend()

figure.tight_layout()
figure.savefig("output/01_scatter_plot.png", dpi=200)
plt.close(figure)

print("Scatter plot saved to output/01_scatter_plot.png")
