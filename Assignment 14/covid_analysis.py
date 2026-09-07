import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


os.makedirs("output", exist_ok=True)

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])
print("Dataset shape:", data_frame.shape)

cleaned_frame = data_frame.drop_duplicates().copy()
numeric_columns = ["Confirmed", "Recovered", "Deaths", "Active"]
for column in numeric_columns:
    cleaned_frame[column] = pd.to_numeric(cleaned_frame[column], errors="coerce")

cleaned_frame["Active"] = cleaned_frame["Active"].fillna(
    cleaned_frame["Confirmed"] - cleaned_frame["Recovered"] - cleaned_frame["Deaths"]
)
cleaned_frame[numeric_columns] = cleaned_frame[numeric_columns].fillna(0)

print("Shape after cleaning:", cleaned_frame.shape)
print("\nData types:")
print(cleaned_frame.dtypes)

latest_state_totals = (
    cleaned_frame.sort_values("Date")
    .groupby("State", as_index=False)
    .tail(1)
    .sort_values("Confirmed", ascending=False)
)

print("\nState-wise totals:")
print(latest_state_totals[["State", "Confirmed", "Recovered", "Deaths", "Active"]])

highest_impacted_state = latest_state_totals.iloc[0]
lowest_impacted_state = latest_state_totals.iloc[-1]
print(
    f"\nHighest impacted state: {highest_impacted_state['State']} "
    f"({int(highest_impacted_state['Confirmed'])} confirmed cases)"
)
print(
    f"Lowest impacted state: {lowest_impacted_state['State']} "
    f"({int(lowest_impacted_state['Confirmed'])} confirmed cases)"
)

daily_state_trends = cleaned_frame.groupby(["Date", "State"], as_index=False)["Confirmed"].max()
print("\nDaily trends in confirmed cases:")
print(daily_state_trends.head(10))

top_states = latest_state_totals.head(3)["State"].tolist()
top_state_data = cleaned_frame[cleaned_frame["State"].isin(top_states)].copy()

recovered_chart = latest_state_totals.sort_values("Recovered", ascending=False)
death_chart = latest_state_totals.head(5)

scatter_frame = cleaned_frame.sort_values(["State", "Date"]).copy()
scatter_frame["DailyNewCases"] = scatter_frame.groupby("State")["Confirmed"].diff().fillna(
    scatter_frame["Confirmed"]
)
scatter_frame["DailyRecovered"] = scatter_frame.groupby("State")["Recovered"].diff().fillna(
    scatter_frame["Recovered"]
)

figure, axes = plt.subplots(2, 2, figsize=(14, 10))

for state in top_states:
    state_data = top_state_data[top_state_data["State"] == state].sort_values("Date")
    axes[0, 0].plot(
        state_data["Date"],
        state_data["Confirmed"],
        marker="o",
        label=state,
    )
axes[0, 0].set_title("Confirmed Cases Trend for Top 3 States")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Confirmed Cases")
axes[0, 0].legend()

axes[0, 1].bar(recovered_chart["State"], recovered_chart["Recovered"], color="tab:green")
axes[0, 1].set_title("State-wise Total Recovered Cases")
axes[0, 1].set_ylabel("Recovered Cases")
axes[0, 1].tick_params(axis="x", rotation=20)

axes[1, 0].pie(
    death_chart["Deaths"],
    labels=death_chart["State"],
    autopct="%1.1f%%",
    startangle=90,
)
axes[1, 0].set_title("Deaths Proportion Across Top 5 States")

axes[1, 1].scatter(
    scatter_frame["DailyNewCases"],
    scatter_frame["DailyRecovered"],
    color="tab:red",
)
axes[1, 1].set_title("Daily New Cases vs Daily Recovered")
axes[1, 1].set_xlabel("Daily New Cases")
axes[1, 1].set_ylabel("Daily Recovered")

figure.tight_layout()
figure.savefig("output/covid_impact_analysis.png", dpi=200)
plt.close(figure)

print("\nPlot saved to output/covid_impact_analysis.png")
