import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("output", exist_ok=True)

numeric_columns = ["Confirmed", "Recovered", "Deaths", "Active"]

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"]).drop_duplicates()
for column in numeric_columns:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")
data_frame["Active"] = data_frame["Active"].fillna(data_frame["Confirmed"] - data_frame["Recovered"] - data_frame["Deaths"])
data_frame[numeric_columns] = data_frame[numeric_columns].fillna(0)

scatter_frame = data_frame.sort_values(["State", "Date"]).copy()
scatter_frame["DailyNewCases"] = scatter_frame.groupby("State")["Confirmed"].diff().fillna(scatter_frame["Confirmed"])
scatter_frame["DailyRecovered"] = scatter_frame.groupby("State")["Recovered"].diff().fillna(scatter_frame["Recovered"])

figure, axes = plt.subplots(figsize=(8, 6))
axes.scatter(scatter_frame["DailyNewCases"], scatter_frame["DailyRecovered"], color="tab:red")
axes.set(title="Daily New Cases vs Daily Recovered", xlabel="Daily New Cases", ylabel="Daily Recovered")

figure.tight_layout()
figure.savefig("output/10_scatter_new_vs_recovered.png", dpi=200)
plt.close(figure)

print("Scatter plot saved to output/10_scatter_new_vs_recovered.png")
