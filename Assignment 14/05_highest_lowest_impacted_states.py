import pandas as pd

numeric_columns = ["Confirmed", "Recovered", "Deaths", "Active"]

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"]).drop_duplicates()
for column in numeric_columns:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")
data_frame["Active"] = data_frame["Active"].fillna(data_frame["Confirmed"] - data_frame["Recovered"] - data_frame["Deaths"])
data_frame[numeric_columns] = data_frame[numeric_columns].fillna(0)

latest_state_totals = data_frame.sort_values("Date").groupby("State", as_index=False).tail(1).sort_values("Confirmed", ascending=False)

highest_impacted_state, lowest_impacted_state = latest_state_totals.iloc[0], latest_state_totals.iloc[-1]
print(f"Highest impacted state: {highest_impacted_state['State']} ({int(highest_impacted_state['Confirmed'])} confirmed cases)")
print(f"Lowest impacted state: {lowest_impacted_state['State']} ({int(lowest_impacted_state['Confirmed'])} confirmed cases)")
