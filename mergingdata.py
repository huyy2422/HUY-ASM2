import pandas as pd
df1 = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet1")
df2 = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet2")
pd.set_option('display.max_rows', 120)
print(df1,df2)