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
axes.hist(frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes.set(title="Histogram", xlabel="Attendance", ylabel="Frequency")

figure.tight_layout()
figure.savefig("output/04_histogram.png", dpi=200)
plt.close(figure)

print("Histogram saved to output/04_histogram.png")
