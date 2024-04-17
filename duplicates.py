import pandas as pd
df = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet1")
pd.set_option('display.max_rows', 120)
duplicate = df.duplicated()
df = df.drop(df[duplicate].index)
df= df.dropna()
print(df)