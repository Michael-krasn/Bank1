import pandas as pd

exel_data = pd.read_excel('transactions_excel.xlsx')
csv_data = pd.read_csv('transactions.csv')

print(exel_data.shape)
print(exel_data.head())
print(csv_data.shape)
print(csv_data.head())
