import pandas as pd

# 1) Configuración de rutas y tipos
FILE_COOLERS   = 'coolers.zip'
FILE_WARNINGS  = 'warnings.csv'
OUT_FILE       = 'coolers_filtrados.csv'
CHUNK_SIZE     = 200_000   # ajusta según tu RAM

# 2) Leemos sólo la columna cooler_id de warnings para crear un set de IDs
warnings_df = pd.read_csv(FILE_WARNINGS, usecols=['cooler_id'], dtype=str)
ids_warning = set(warnings_df['cooler_id'].str.strip())

# 3) Preparamos el archivo de salida (borramos si existe y escribimos header en el primer chunk)
first_chunk = True

# 4) Leemos coolers en chunks y filtramos
for chunk in pd.read_csv(FILE_COOLERS, chunksize=CHUNK_SIZE, dtype=str):
    # Aseguramos que cooler_id está limpito
    chunk['cooler_id'] = chunk['cooler_id'].str.strip()
    # Filtramos sólo los IDs que están en warnings
    filtered = chunk[chunk['cooler_id'].isin(ids_warning)]
    if not filtered.empty:
        # Appendeamos al CSV de salida
        filtered.to_csv(
            OUT_FILE,
            mode='a',
            index=False,
            header=first_chunk
        )
        first_chunk = False

print(f'Filtrado completado. Resultado en "{OUT_FILE}" con {pd.read_csv(OUT_FILE).shape[0]} filas.')
