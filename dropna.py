import pandas as pd
df = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet1")
pd.set_option('display.max_rows', 120)
df= df.dropna()
print(df)
