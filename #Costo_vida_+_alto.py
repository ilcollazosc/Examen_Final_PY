import pandas as pd
datos = pd.read_csv('living.csv')
costo_mas_alto = datos.loc[datos['Cost of living, 2017'].idxmax(), 'Countries']
print(costo_mas_alto)
