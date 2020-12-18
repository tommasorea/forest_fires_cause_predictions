import pandas as pd


filepath = "../data/fires2015_train.csv"

# Read the file into a variable fifa_data
df = pd.read_csv(filepath, parse_dates=True)


print(df.head(10))