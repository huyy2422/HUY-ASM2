import pandas as pd
df = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet2")
pd.set_option('display.max_rows', 120)
filltered_df = df[df['Order Quantity'] >11]
print(filltered_df)
