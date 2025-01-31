import pandas as pd
datos = pd.read_csv('living.csv')
costo_vida_peru = datos[datos['Countries'] == 'Peru']
costo_vida_peru = costo_vida_peru['Global rank']
print(costo_vida_peru)
