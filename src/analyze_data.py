import os
from collections import Counter
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Descargar recursos de NLTK si no están disponibles
nltk.download("vader_lexicon")
nltk.download("punkt")
nltk.download("stopwords")

# Definir un diccionario de sinónimos para agrupar palabras similares
SINONIMOS = {
    "habitación": ["habitación", "habitacion", "habitaciones", "room", "cuarto"],
    "atención": ["atención", "atencion", "personal", "staff", "servicio", "amable", "amabilidad", "friendly", "atento", "atenta"],
    "ubicación": ["ubicación", "ubicacion", "location", "cerca", "lejos", "lugar", "zona"],
    "desayuno": ["desayuno", "breakfast"],
    "hotel": ["hotel", "instalaciones", "hostel"],
    "baño": ["baño", "bathroom"],
    "ruido": ["ruido", "noise"],
    "agua": ["agua", "water"],
    "limpieza": ["limpieza", "limpio", "limpia", "clean"],
    "comodidad": ["comodidad", "cómodas", "comoda", "cómoda", "cómodo"],
    "precio": ["precio", "costo", "valor"],
    "cama": ["cama", "camas", "lecho", "acomodación"],
    "comida": ["comida", "alimentos"]
}

# Crear un mapeo inverso de cada palabra a su clave común
MAPEO_SINONIMOS = {variante: clave for clave, variantes in SINONIMOS.items() for variante in variantes}

class DataAnalyzer:
    def __init__(self, data):
        self.data = data.copy()  # Trabajamos sobre una copia del DataFrame
        self.analyzer = SentimentIntensityAnalyzer()

        # Cargar stopwords en español e inglés
        stop_words_es = set(stopwords.words("spanish"))
        stop_words_en = set(stopwords.words("english"))
        self.stop_words = stop_words_es.union(stop_words_en)

        # Palabras irrelevantes que no aportan valor analítico
        self.palabras_excluir = {
            "excelente", "great", "falta", "solo", "super", "súper", "buena", "bueno",
            "buen", "bien", "sí", "si", "no", "muy", "más", "menos", "gran",
            "noche", "día", "regular", "mal", "good", "bad", "especificado",
            "nice", "linda", "lindo", "perfecto", "gusto", "gustó", "nada", "nothing",
            "siempre", "mas", "más", "et", "ser", "everything", "toda", "todo", "mejorar",
            "tener", "tiene", "could", "não", "No especificado"
        }

    def preprocess_text(self, text):
        """ Tokeniza, filtra y normaliza palabras en el texto. """
        if not isinstance(text, str):
            return []

        words = word_tokenize(text.lower())
        filtered_words = [w for w in words if w.isalnum() and w not in self.stop_words and w not in self.palabras_excluir]
        return [MAPEO_SINONIMOS.get(w, w) for w in filtered_words]

    def analyze(self):
        """ Realiza análisis de datos, sentimiento y palabras clave. """

        print("\n📊 Análisis general de los datos:")
        print(self.data.describe(include="all"))

        # Verificar si existen las columnas necesarias
        if not all(col in self.data.columns for col in ["Cosas Positivas", "Cosas Negativas", "Grupo viaje"]):
            raise ValueError("El DataFrame debe contener las columnas 'Cosas Positivas', 'Cosas Negativas' y 'Grupo viaje'.")

        # Unir comentarios y analizar sentimiento
        print("\n💬 Análisis de sentimiento:")
        self.data["Cosas Positivas"] = self.data["Cosas Positivas"].fillna("")
        self.data["Cosas Negativas"] = self.data["Cosas Negativas"].fillna("")
        self.data["Comentarios"] = self.data["Cosas Positivas"] + " " + self.data["Cosas Negativas"]
        self.data["Sentimiento"] = self.data["Comentarios"].apply(lambda x: self.analyzer.polarity_scores(x)["compound"])

        # Extraer palabras clave positivas y negativas
        self.data["Palabras_clave_positivas"] = self.data["Cosas Positivas"].apply(self.preprocess_text)
        self.data["Palabras_clave_negativas"] = self.data["Cosas Negativas"].apply(self.preprocess_text)

        print("\n📌 Análisis por grupo de viaje:")
        resultados_por_grupo = []

        for grupo, data_grupo in self.data.groupby("Grupo viaje"):
            print(f"\n🧳 Grupo de viaje: {grupo}")

            data_grupo["Calificación"] = pd.to_numeric(data_grupo["Calificación"], errors="coerce")
            descripcion_calificacion = data_grupo["Calificación"].describe()
            print(descripcion_calificacion)

            # Contar palabras clave positivas y negativas
            palabras_positivas = [palabra for lista in data_grupo["Palabras_clave_positivas"] for palabra in lista]
            palabras_negativas = [palabra for lista in data_grupo["Palabras_clave_negativas"] for palabra in lista]

            top_positivas = Counter(palabras_positivas).most_common(10)
            top_negativas = Counter(palabras_negativas).most_common(10)

            print("\n🔹 Palabras positivas más frecuentes:", top_positivas)
            print("🔸 Palabras negativas más frecuentes:", top_negativas)

            resultados_por_grupo.append({
                "Grupo viaje": grupo,
                "count": descripcion_calificacion["count"],
                "mean": descripcion_calificacion["mean"],
                "std": descripcion_calificacion["std"],
                "min": descripcion_calificacion["min"],
                "25%": descripcion_calificacion["25%"],
                "50%": descripcion_calificacion["50%"],
                "75%": descripcion_calificacion["75%"],
                "max": descripcion_calificacion["max"],
                "Palabras positivas más frecuentes": top_positivas,
                "Palabras negativas más frecuentes": top_negativas
            })

        # Guardar resultados
        os.makedirs("data/results", exist_ok=True)

        try:
            output_path_general = "data/results/analisis_general.csv"
            self.data.describe(include="all").to_csv(output_path_general)
            print(f"\n📂 Análisis general guardado en: {os.path.abspath(output_path_general)}")
        except Exception as e:
            print(f"❌ Error al guardar el análisis general: {e}")

        try:
            output_path_grupo = "data/results/analisis_por_grupo.csv"
            resultados_por_grupo_df = pd.DataFrame(resultados_por_grupo)
            resultados_por_grupo_df.to_csv(output_path_grupo, index=False)
            print(f"📂 Análisis por grupo de viaje guardado en: {os.path.abspath(output_path_grupo)}")
        except Exception as e:
            print(f"❌ Error al guardar el análisis por grupo de viaje: {e}")

        try:
            output_path_sentimiento = "data/results/analisis_sentimiento.csv"
            self.data[["Grupo viaje", "Comentarios", "Sentimiento", "Palabras_clave_positivas", "Palabras_clave_negativas"]].to_csv(output_path_sentimiento, index=False)
            print(f"📂 Análisis de sentimiento guardado en: {os.path.abspath(output_path_sentimiento)}")
        except Exception as e:
            print(f"❌ Error al guardar el análisis de sentimiento: {e}")