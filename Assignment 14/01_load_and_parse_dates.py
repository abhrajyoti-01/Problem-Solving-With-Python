import pandas as pd

data_frame = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])

print("Dataset shape:", data_frame.shape)
print("\nFirst 5 records:")
print(data_frame.head())
print(f"\nDate column data type: {data_frame['Date'].dtype}")
