# Visual Studio Code Debug Configuration 
{
  "configurations": [
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch Program",
      "program": "${workspaceFolder}/prueba.py"
    }
  ]
}

# abrir los archivos con el copy path 
coolers = 'coolers.zip'
calendar = 'calendar.csv'
sales = 'sales.zip'
warning = 'warnings.csv'

# importar las librerías y leer los archivos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Coolers = pd.read_csv(coolers, sep = ';') #aquí lees los archivos csv y separas las columnas con ;
Coolers.head()

Calendar = pd.read_csv(calendar, sep = ';')
Calendar.head()

Sales = pd.read_csv(sales, sep = ';')
Sales.head()

Warning = pd.read_csv(warning, sep = ';')
Warning.head()

# conversión a array de cada uno de los archivos csv

coolers = Coolers.to_numpy()
calendar = Calendar.to_numpy()
sales = Sales.to_numpy()
warning = Warning.to_numpy()

# impresión de los headings de las columnas de cada uno de los arreglos

print(Coolers.columns)
print(Calendar.columns)
print(Sales.columns)
print(Warning.columns)

# extracción de los valores de las columnas repetidas

coolers_coolerID = coolers[:,0]
sales_coolerID = sales[:,0]
warning_coolerID = warning[:,0]


