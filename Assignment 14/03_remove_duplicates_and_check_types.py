import pandas as pd

numeric_columns = ["Confirmed", "Recovered", "Deaths", "Active"]

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])

print(f"Shape before removing duplicates: {data_frame.shape}")
data_frame = data_frame.drop_duplicates()
print(f"Shape after removing duplicates: {data_frame.shape}")

for column in numeric_columns:
    data_frame[column] = pd.to_numeric(data_frame[column], errors="coerce")

print("\nData types:")
print(data_frame.dtypes)
