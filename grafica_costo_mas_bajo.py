import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('living.csv')

# Ordenando datos de forma ascendente (top 10)
top_10_paises = datos.sort_values(by='Cost of living, 2017', ascending=True).head(10)

# Grafica
plt.figure(figsize=(10, 6)) 
plt.bar(top_10_paises['Countries'], top_10_paises['Cost of living, 2017'], color='skyblue')
plt.xlabel('Países')
plt.ylabel('Costo de vida')
plt.title('Top 10 países con el costo de vida más bajo')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()