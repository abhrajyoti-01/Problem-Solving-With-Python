import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

frame = pd.read_csv("data/visualization_data.csv")

pair_plot = sns.pairplot(frame[["StudyHours", "Marks", "Attendance"]])
pair_plot.fig.suptitle("Pair Plot", y=1.02)
pair_plot.savefig("output/06_pair_plot.png", dpi=200)
plt.close(pair_plot.fig)

print("Pair plot saved to output/06_pair_plot.png")
