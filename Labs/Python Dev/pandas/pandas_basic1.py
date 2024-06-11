import pandas as pd
import csv

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

print(df)