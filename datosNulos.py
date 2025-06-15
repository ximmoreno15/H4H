# Código para: identificar los valores NaN en cada columna de cada fila del coolers_con_binary_warning

import pandas as pd #importar librerías

coolers_con_binary_warning = pd.read_csv("coolers_con_binary_warning.csv")

print("\nValores Nan antes de procesar los datos:\n")

print(coolers_con_binary_warning.isnull().sum())

# Para imputar los valores NaN, rellenar NaN con media de cada columna numérica
for column in coolers_con_binary_warning.select_dtypes(include=['float64', 'int64']).columns: