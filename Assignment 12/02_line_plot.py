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
axes.plot(frame["Month"], frame["Marks"], color="tab:green", marker="o", label="Marks Trend")
axes.set(title="Line Plot", xlabel="Month", ylabel="Marks")
axes.legend()

figure.tight_layout()
figure.savefig("output/02_line_plot.png", dpi=200)
plt.close(figure)

print("Line plot saved to output/02_line_plot.png")
