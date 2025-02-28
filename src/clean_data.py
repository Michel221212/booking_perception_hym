import pandas as pd 

class DataCleaner:
    def __init__(self, data):
        self.data = data.copy()  # Evita modificar el DataFrame original

    def clean_data(self):
        """
        Realiza la limpieza de los datos y proporciona métricas del proceso.
        """

        # --- Antes de la limpieza ---
        rows_before = len(self.data)
        print(f"📌 Total de filas antes de la limpieza: {rows_before}")

        # Verificar valores nulos antes
        null_values_before = self.data.isnull().sum()
        print("\n🔍 Valores nulos por columna antes de la limpieza:\n", null_values_before)

        # Eliminar columna innecesaria si existe
        if "Unnamed: 0" in self.data.columns:
            self.data.drop(columns=["Unnamed: 0"], inplace=True)
            print("🗑️ Se eliminó la columna 'Unnamed: 0'.")

        # Convertir "Calificación" a numérico si es posible
        if "Calificación" in self.data.columns:
            self.data["Calificación"] = pd.to_numeric(self.data["Calificación"], errors="coerce")
            print("🔄 Se convirtió la columna 'Calificación' a tipo numérico.")

            # Crear la columna 'Etiqueta' basada en la 'Calificación' solo si no es NaN
            self.data["Etiqueta"] = self.data["Calificación"].apply(
                lambda x: "Positiva" if pd.notna(x) and x >= 8 else 
                          ("Negativa" if pd.notna(x) and x <= 4 else "Neutral" if pd.notna(x) else "Desconocida")
            )
            print("🏷️ Se creó la columna 'Etiqueta' basada en la 'Calificación'.")

        # Eliminar filas duplicadas
        duplicates_before = self.data.duplicated().sum()
        self.data.drop_duplicates(inplace=True)
        duplicates_after = self.data.duplicated().sum()
        print(f"♻️ Se eliminaron {duplicates_before - duplicates_after} filas duplicadas.")

        # Rellenar valores nulos en columnas de texto si existen
        text_columns = ["Cosas Positivas", "Cosas Negativas", "Titulo"]
        existing_text_columns = [col for col in text_columns if col in self.data.columns]
        if existing_text_columns:
            self.data[existing_text_columns] = self.data[existing_text_columns].fillna("No especificado")
            print(f"✍️ Se reemplazaron valores nulos en columnas de texto: {existing_text_columns}")

        # --- NUEVO: Combinar 'Cosas Positivas' y 'Cosas Negativas' en 'Opiniones' ---
        if {"Cosas Positivas", "Cosas Negativas"}.issubset(self.data.columns):
            self.data["Opiniones"] = self.data[["Cosas Positivas", "Cosas Negativas"]].astype(str).agg(" ".join, axis=1)
            print("📝 Se creó la columna 'Opiniones' combinando 'Cosas Positivas' y 'Cosas Negativas'.")

        # --- Después de la limpieza ---
        rows_after = len(self.data)
        print(f"\n📌 Total de filas después de la limpieza: {rows_after}")

        # Verificar valores nulos después
        null_values_after = self.data.isnull().sum()
        print("\n🔍 Valores nulos por columna después de la limpieza:\n", null_values_after)

        # Métricas de limpieza
        rows_removed = rows_before - rows_after
        reduction_percentage = (rows_removed / rows_before) * 100 if rows_before > 0 else 0
        print(f"\n✅ Filas eliminadas: {rows_removed} ({reduction_percentage:.2f}%)")

        print("\n🎯 ¡Datos limpiados exitosamente! 🎯")
        return self.data