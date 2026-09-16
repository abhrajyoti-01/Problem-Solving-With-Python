import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("output", exist_ok=True)

data_frame = pd.read_csv("data/student_records.csv")
data_frame["Attendance"] = pd.to_numeric(data_frame["Attendance"], errors="coerce")
data_frame["Attendance"] = data_frame["Attendance"].fillna(data_frame["Attendance"].median())

figure, axes = plt.subplots(figsize=(8, 6))
axes.hist(data_frame["Attendance"], bins=5, color="tab:orange", edgecolor="black")
axes.set(title="Attendance Distribution", xlabel="Attendance Percentage", ylabel="Frequency")

figure.tight_layout()
figure.savefig("output/08_histogram_attendance.png", dpi=200)
plt.close(figure)

print("Histogram saved to output/08_histogram_attendance.png")
