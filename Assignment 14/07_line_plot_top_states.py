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

latest_state_totals = data_frame.sort_values("Date").groupby("State", as_index=False).tail(1).sort_values("Confirmed", ascending=False)
top_states = latest_state_totals.head(3)["State"].tolist()
top_state_data = data_frame[data_frame["State"].isin(top_states)]

figure, axes = plt.subplots(figsize=(9, 6))
for state in top_states:
    state_data = top_state_data[top_state_data["State"] == state].sort_values("Date")
    axes.plot(state_data["Date"], state_data["Confirmed"], marker="o", label=state)
axes.set(title="Confirmed Cases Trend for Top 3 States", xlabel="Date", ylabel="Confirmed Cases")
axes.legend()

figure.tight_layout()
figure.savefig("output/07_line_plot_top_states.png", dpi=200)
plt.close(figure)

print("Line plot saved to output/07_line_plot_top_states.png")
