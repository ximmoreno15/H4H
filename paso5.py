import pandas as pd
from sklearn.model_selection import train_test_split

# Replace the path with the actual location if needed
df_coolers = pd.read_csv('coolers_con_binary_warning_imputed.csv')

# Display the first few rows to verify
print(df_coolers.head())

features = [
    'door_opens',
    'open_time',
    'compressor',
    'power',
    'on_time',
    'min_voltage',
    'max_voltage',
    'temperature'
]

X = df_coolers[features] # Variables de entrada
y = df_coolers['binary_warning'] # Variable de salida

print(f"Variables de entrada (X) seleccionadas: {X.columns.tolist()}")
print(f"Variable de salida (y) seleccionada: {y.name}")
print(f"Dimensiones de X: {X.shape}")
print(f"Dimensiones de y: {y.shape}")

# Dividir los datos en conjuntos de entrenamiento y prueba
# test_size=0.30 significa que el 30% de los datos se usarán para prueba y el 70% para entrenamiento.
# random_state asegura que la división sea la misma cada vez que ejecutes el código, para reproducibilidad.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print(f"\nDimensiones del conjunto de entrenamiento (X_train): {X_train.shape}")
print(f"Dimensiones del conjunto de prueba (X_test): {X_test.shape}")
print(f"Dimensiones del conjunto de entrenamiento (y_train): {y_train.shape}")
print(f"Dimensiones del conjunto de prueba (y_test): {y_test.shape}")
