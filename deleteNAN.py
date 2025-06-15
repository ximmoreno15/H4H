import pandas as pd

# Define la ruta de tu archivo CSV de entrada
file_path = "coolers_filtrados.csv"

try:
    # 1. Cargar el archivo CSV en un DataFrame de pandas
    # pandas es excelente para trabajar con datos tabulares y manejar valores faltantes.
    df = pd.read_csv(file_path)

    # Obtenemos el número inicial de filas para comparación
    initial_rows = df.shape[0]

    print("Información inicial del DataFrame:")
    print(df.info()) # Muestra el número de valores no nulos por columna
    print("\nPrimeras 5 filas del DataFrame inicial:")
    print(df.head())

    # 2. Eliminar las filas que contengan cualquier valor NaN
    # El método .dropna() elimina las filas (por defecto, axis=0) o columnas (axis=1)
    # que contienen valores NaN. Aquí, se eliminará la fila completa si cualquier columna tiene NaN.
    df_cleaned = df.dropna()

    # Obtenemos el número de filas después de la limpieza
    cleaned_rows = df_cleaned.shape[0]

    # 3. Definir la ruta y el nombre del nuevo archivo CSV
    output_file_path = "coolers_sin_nan.csv"

    # 4. Guardar el DataFrame limpio en un nuevo archivo CSV
    # index=False es importante para que pandas no escriba el índice del DataFrame como una columna en el CSV.
    df_cleaned.to_csv(output_file_path, index=False)

    print(f"\n--- Proceso Completado ---")
    print(f"Se eliminaron las filas con valores NaN del archivo '{file_path}'.")
    print(f"Número de filas inicial: {initial_rows}")
    print(f"Número de filas después de eliminar NaN: {cleaned_rows}")
    print(f"El archivo limpio se ha guardado exitosamente como '{output_file_path}'")

    print("\nInformación del DataFrame limpio:")
    print(df_cleaned.info()) # Verifica que ya no haya valores nulos
    print("\nPrimeras 5 filas del DataFrame limpio:")
    print(df_cleaned.head())


except FileNotFoundError:
    print(f"Error: El archivo '{file_path}' no se encontró. Por favor, asegúrate de que esté en el mismo directorio.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")