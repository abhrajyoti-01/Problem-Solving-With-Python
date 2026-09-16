import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

frame = pd.read_csv("data/visualization_data.csv")

figure, axes = plt.subplots(figsize=(9, 6))
axes.plot(frame["Month"], frame["Marks"], color="tab:blue", marker="o", linestyle="-", linewidth=2, label="Marks")
axes.plot(frame["Month"], frame["Attendance"], color="tab:red", marker="s", linestyle="--", linewidth=2, label="Attendance")
axes.set(title="Styled Line Plot", xlabel="Month", ylabel="Value")
axes.legend()

figure.tight_layout()
figure.savefig("output/07_styled_plots.png", dpi=200)
plt.close(figure)

print("Styled plot saved to output/07_styled_plots.png")
