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
sns.boxplot(data=frame, y="Marks", x="Category", hue="Category", ax=axes, palette="Set2", legend=False)
axes.set(title="Box Plot", xlabel="Category", ylabel="Marks")

figure.tight_layout()
figure.savefig("output/05_box_plot.png", dpi=200)
plt.close(figure)

print("Box plot saved to output/05_box_plot.png")
