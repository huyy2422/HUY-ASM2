import pandas as pd
df = pd.read_excel("Sales_Data.xlsx", sheet_name="Sheet2")
pd.set_option('display.max_rows', 120)
df["Total Profit"] = pd.to_numeric(df["Total Profit"], errors="coerce").fillna(0)
print(df)
