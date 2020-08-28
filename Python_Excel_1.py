import pandas as pd
from openpyxl.workbook import workbook

df_csv = pd.read_csv('KTCdata.csv')

# print(df_csv)

# print(df_csv.columns)
# print(df_csv.iloc[20,2])
print(df_csv[['Income','Age','Female']])

 print(df_csv.loc[df_csv['Female'] == 1])
print(df_csv.loc[(df_csv['Female'] == 1) & (df_csv['Income'] >= 20000) & (df_csv['Age'] < 40)])
