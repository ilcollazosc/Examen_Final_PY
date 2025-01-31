import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('living.csv')

# datos de AMERICA
paises_america = datos[datos['Continent'] == 'America']

# Grafica
plt.figure(figsize=(10, 6)) 
plt.bar(paises_america['Countries'], paises_america['Cost of living, 2017'], color='skyblue')
plt.xlabel('Países')
plt.ylabel('Costo de vida')
plt.title('Costo de vida en países de América')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()