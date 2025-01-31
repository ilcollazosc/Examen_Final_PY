import pandas as pd
datos=pd.read_csv('living.csv')
costo_vida_promedio=datos['Cost of living, 2017'].mean()
print(costo_vida_promedio)