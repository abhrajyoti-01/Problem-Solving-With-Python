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
death_chart = latest_state_totals.head(5)

figure, axes = plt.subplots(figsize=(8, 6))
axes.pie(death_chart["Deaths"], labels=death_chart["State"], autopct="%1.1f%%", startangle=90)
axes.set_title("Deaths Proportion Across Top 5 States")

figure.tight_layout()
figure.savefig("output/09_pie_chart_deaths.png", dpi=200)
plt.close(figure)

print("Pie chart saved to output/09_pie_chart_deaths.png")
