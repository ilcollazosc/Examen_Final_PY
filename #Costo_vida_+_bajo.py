import pandas as pd
datos = pd.read_csv('living.csv')
costo_mas_bajo = datos.loc[datos['Cost of living, 2017'].idxmin(), 'Countries']
print(costo_mas_bajo)
