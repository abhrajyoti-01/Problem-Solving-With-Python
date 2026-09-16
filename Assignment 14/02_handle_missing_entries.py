import pandas as pd

numeric_columns = ["Confirmed", "Recovered", "Deaths", "Active"]

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])
for column in numeric_columns:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")

print("Missing values before handling:")
print(data_frame[numeric_columns].isna().sum())

data_frame["Active"] = data_frame["Active"].fillna(data_frame["Confirmed"] - data_frame["Recovered"] - data_frame["Deaths"])
data_frame[numeric_columns] = data_frame[numeric_columns].fillna(0)

print("\nMissing values after handling:")
print(data_frame[numeric_columns].isna().sum())
