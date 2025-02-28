import os
import argparse
from load_data import DataLoader
from clean_data import DataCleaner
from analyze_data import DataAnalyzer
import train_models  # Importamos aquí para asegurarnos de que se usen correctamente las funciones

def ensure_directory_exists(directory):
    """ Crea el directorio si no existe """
    if not os.path.exists(directory):
        os.makedirs(directory)

def main(file_path="data/raw/reviews_booking.csv"):
    """
    Función principal que ejecuta el proceso de carga, limpieza, análisis y entrenamiento de modelos.
    """
    try:
        # Cargar datos
        print("\n🔹 Cargando datos...")
        loader = DataLoader(file_path)
        data = loader.load_data()

        if data is not None:
            print(f"\n✅ Datos cargados: {data.shape[0]} filas, {data.shape[1]} columnas")

            # Limpiar datos
            print("\n🔹 Limpiando datos...")
            cleaner = DataCleaner(data)
            cleaned_data = cleaner.clean_data()
            print(f"✅ Datos limpios: {cleaned_data.shape[0]} filas, {cleaned_data.shape[1]} columnas")

            # Combinar 'Cosas Positivas' y 'Cosas Negativas' en una nueva columna 'Opiniones'
            cleaned_data["Opiniones"] = cleaned_data[["Cosas Positivas", "Cosas Negativas"]].astype(str).agg(" ".join, axis=1)

            # Guardar datos limpios en la carpeta 'processed'
            output_path = "data/processed/cleaned_data.csv"
            ensure_directory_exists(os.path.dirname(output_path))
            cleaned_data.to_csv(output_path, index=False)
            print(f"\n✅ Datos limpios guardados en '{output_path}'.")

            # Analizar datos
            print("\n🔹 Analizando datos...")
            analyzer = DataAnalyzer(cleaned_data)
            analyzer.analyze()

            # Entrenar modelo no supervisado (K-Means) y obtener el vectorizador
            print("\n🔹 Entrenando modelo no supervisado (K-Means)...")
            cleaned_data, X, kmeans, vectorizer = train_models.train_unsupervised_model(cleaned_data)

            # Entrenar modelos supervisados pasándole el vectorizador
            print("\n🔹 Entrenando modelos supervisados...")
            train_models.train_supervised_models(cleaned_data, vectorizer)

            print("\n✅ Proceso completado con éxito.")

    except Exception as e:
        print(f"\n❌ Error en la ejecución: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", nargs="?", default="data/raw/reviews_booking.csv", help="Ruta del archivo CSV con los datos")
    args = parser.parse_args()
    
    main(args.file_path)