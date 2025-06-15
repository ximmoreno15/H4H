import pandas as pd

coolers_con_binary_warning = pd.read_csv("coolers_con_binary_warning.csv")

print("\nValores NaN antes de procesar los datos:\n")
print(coolers_con_binary_warning.isnull().sum())

# Imputar valores NaN con la media
for column in coolers_con_binary_warning.select_dtypes(include=['float64', 'int64']).columns:
    if coolers_con_binary_warning[column].isnull().sum() > 0:
        # Rellenar con la media
        mean_value = coolers_con_binary_warning[column].mean()
        coolers_con_binary_warning[column].fillna(mean_value, inplace=True)
        print(f"Columna '{column}' imputada con la media: {mean_value:.2f}")

print("\nValores NaN después de procesar los datos:\n")
print(coolers_con_binary_warning.isnull().sum())

# Verificación
print("\nVerificación de valores NaN en columnas numéricas:\n")
print(coolers_con_binary_warning.select_dtypes(include=['float64', 'int64']).isnull().sum())

# Guardar archivo
coolers_con_binary_warning.to_csv("coolers_con_binary_warning_imputed.csv", index=False)
print("\nDatos procesados y guardados en 'coolers_con_binary_warning_imputed.csv'.")
