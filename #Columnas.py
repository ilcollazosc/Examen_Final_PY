import pandas as pd
df = pd.read_csv('living.csv')
num_columnas = len(df.columns)
print(num_columnas)