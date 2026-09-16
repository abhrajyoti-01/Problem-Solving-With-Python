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

latest_state_totals = data_frame.sort_values("Date").groupby("State", as_index=False).tail(1).sort_values("Recovered", ascending=False)

figure, axes = plt.subplots(figsize=(9, 6))
axes.bar(latest_state_totals["State"], latest_state_totals["Recovered"], color="tab:green")
axes.set(title="State-wise Total Recovered Cases", xlabel="State", ylabel="Recovered Cases")
axes.tick_params(axis="x", rotation=20)

figure.tight_layout()
figure.savefig("output/08_bar_chart_recovered.png", dpi=200)
plt.close(figure)

print("Bar chart saved to output/08_bar_chart_recovered.png")
