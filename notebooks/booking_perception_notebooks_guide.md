<div style="text-align: center;">
<image src="../docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# 📊 Exploración y Análisis de Datos

## 🔍 Exploración inicial de Datos

La exploración inicial de los datos es crucial para comprender la estructura y calidad de la información. Dentro del proyecto, se han realizado las siguientes acciones:

### 📥 Carga y visualización de datos crudos

- Se cargaron **438,213 registros con 12 columnas** desde `data/raw/reviews_booking.csv`.
- Se analizaron los **tipos de datos** y la **presencia de valores nulos**.
- Se identificaron los siguientes datos nulos: **"País" (1,972), "Acomodación" (418,310), "Grupo viaje" (2), "Título" (661), "Cosas Positivas" (201,357) y "Cosas Negativas" (258,200)**.

### 🛠️ Manejo de valores nulos

- Se **eliminó la columna "Unnamed: 0"** ya que no aportaba información relevante.
- Se convirtió la columna **'Calificación' a tipo numérico**.
- Se **eliminaron filas con valores nulos en 'Calificación'**, dado que es una variable crítica para el análisis.
- Se **creó la columna 'Etiqueta'** basada en la 'Calificación' para categorizar las reseñas.
- Se **eliminaron 63,609 filas duplicadas**.
- Se **reemplazaron los valores nulos en las columnas de texto** ('Cosas Positivas', 'Cosas Negativas', 'Titulo') por "No especificado".
- Se **creó la columna 'Opiniones'** que contiene la concatenación de las columnas 'Cosas Positivas' y 'Cosas Negativas'.

### 📊 Revisión de distribuciones

- Se analizaron las **variables categóricas y numéricas**, identificando patrones en `Grupo de Viaje`, `Calificación` y `Fecha de Reseña`.
- Se **eliminaron 236,637 filas con valores nulos en 'Calificación'** durante el proceso de limpieza.
- Se **eliminaron 63,609 filas duplicadas** durante el proceso de limpieza.
- Se **redujo el dataset de 438,213 filas a 374,604 filas** (14.52%).
- Los resultados se guardaron en `data/processed/cleaned_data.csv`.

---

## 📈 Creación de análisis y visualizaciones interactivas

Para facilitar la interpretación de los datos, se generaron **visualizaciones y análisis específicos**:

### ⭐ Distribución de calificaciones

- Se identificó una **tendencia hacia calificaciones de 10**, en todos los grupos de viaje sin variación. Esto podría indicar **sesgo en la calificación**.

### 📝 Análisis de palabras clave

- Se extrajeron las palabras más frecuentes en `Cosas Positivas` y `Cosas Negativas` para cada grupo de viaje. Algunas de las palabras más comunes son:
    - **Positivas:** "atención", "ubicación", "hotel", "desayuno", "habitación", "limpieza", "comodidad".
    - **Negativas:** "habitación", "desayuno", "atención", "hotel", "ubicación", "baño", "agua", "ruido".

### 🏷️ Análisis por grupo de viaje

- Se analizaron **patrones de calificación según Grupo de Viaje**, mostrando **puntuaciones consistentemente altas** en todos los segmentos, lo que podría indicar sesgo en la recolección de datos.

Estos análisis se documentaron en:

- 📂 `data/results/analisis_general.csv`
- 📂 `data/results/analisis_por_grupo.csv`

---

## 🤖 Pruebas y prototipado de modelos de Machine Learning

El proyecto incluye el desarrollo y evaluación de **modelos predictivos** para analizar la percepción de los usuarios.

### 🔄 Preprocesamiento de datos

- **Normalización y tokenización** de textos de reseñas.
- **Vectorización** de `Opiniones` (creada a partir de `Cosas Positivas` y `Cosas Negativas`) mediante **TF-IDF**.

### 🏆 Modelos explorados

- 🔹 **Clasificadores** para predecir la satisfacción del usuario basados en `reseña` y `Calificación`, aunque la mayoría de las calificaciones son **10**, lo que podría afectar la calidad del modelo. Los modelos utilizados fueron Naïve Bayes, Random Forest y XGBoost, todos con un accuracy de alrededor de 0.38. Se excluyó el modelo LSTM debido a su bajo rendimiento.
- 🔹 **Modelos de clustering** para identificar **patrones en la experiencia del usuario**. Se utilizó K-Means.
- 🔹 **Modelos de análisis de sentimiento**, evaluando la **polaridad de las opiniones**, donde se observó un predominio de términos positivos en general.

### 📊 Evaluación de modelos

- Se midieron métricas como **precisión, recall y F1-score**.
- Se compararon diferentes enfoques para **mejorar la interpretabilidad** de los resultados.

📌 **Los modelos y sus desempeños se documentaron en:**
- 📂 `reports/model_evaluation/model_evaluation.md`