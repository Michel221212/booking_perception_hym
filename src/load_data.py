import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path):
        # Convertir ruta a absoluta en caso de que sea relativa
        self.file_path = os.path.abspath(file_path)

    def load_data(self, n_rows=None, sep=None):
        """
        Carga los datos desde un archivo CSV y muestra información sobre los datos cargados.

        Parámetros:
        - n_rows (int, opcional): Número de filas a cargar (útil para archivos grandes).
        - sep (str, opcional): Separador de columnas (si se conoce, mejora la carga).

        Retorna:
        - pd.DataFrame si la carga es exitosa, None en caso de error.
        """
        if not os.path.exists(self.file_path):
            print(f"❌ Error: El archivo '{self.file_path}' no existe.")
            return None
        
        try:
            # Si no se especifica el separador, intentamos detectar automáticamente
            sep_detected = sep if sep else ("," if self.file_path.endswith(".csv") else None)

            # Intentar cargar el archivo con diferentes encodings si es necesario
            try:
                df = pd.read_csv(self.file_path, encoding="utf-8", sep=sep_detected, low_memory=False, nrows=n_rows)
            except UnicodeDecodeError:
                df = pd.read_csv(self.file_path, encoding="latin1", sep=sep_detected, low_memory=False, nrows=n_rows)

            print("✅ Datos cargados exitosamente.")

            # Mostrar información general sobre los datos
            print("\n📊 Información general de los datos:")
            df.info(memory_usage="deep")

            # Mostrar las primeras filas del DataFrame
            num_preview = min(5, len(df))  # Asegura que no intente mostrar más de lo disponible
            print("\n📝 Primeras filas del DataFrame:")
            print(df.head(num_preview).to_markdown(index=False, numalign="left", stralign="left"))

            return df

        except Exception as e:
            print(f"❌ Error al cargar los datos: {e}")
            return None