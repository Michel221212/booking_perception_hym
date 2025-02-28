<div style="text-align: center;">
<image src="../docs/images/encabezado.png" alt="EAN + Booking.com" width="800" height="83">
</div>

# 📊 Datos en el Proyecto

**📁 data/**

Directorio de almacenamiento de datos en diferentes etapas del proceso.

* **📂 raw/** → Datos sin procesar.

    * **📄 reviews_booking.csv:** Archivo de datos crudos, con 438,213 filas y 12 columnas. Contiene información sobre reseñas de hoteles, como país, tipo de alojamiento, fechas de hospedaje y reseña, calificación, título de la reseña, aspectos positivos y negativos, entre otros.

* **📂 processed/** → Datos limpios y listos para el análisis.

    * **📄 cleaned_data.csv:** Datos después del preprocesamiento, con 374,604 filas y 13 columnas (se agregó la columna "Etiqueta"). Se eliminaron filas duplicadas y valores nulos en la columna 'Calificación', se convirtió la columna `Calificación` a numérica, se creó la columna `Etiqueta` basada en la calificación y se imputaron valores nulos en columnas de texto.

* **📂 results/** → Resultados de los análisis.

    * **📄 analisis_general.csv:** Resultados de análisis descriptivo general de los datos, incluyendo estadísticas como la media, desviación estándar, mínimo, máximo y percentiles para las variables numéricas, y la frecuencia y porcentaje para las variables categóricas.

    * **📄 analisis_por_grupo.csv:** Análisis por grupo de viaje (En familia, En grupo, En pareja, Persona que viaja sola), incluyendo estadísticas descriptivas de la calificación para cada grupo de viaje, así como las palabras clave más frecuentes en las reseñas positivas y negativas.

    * **📄 analisis_sentimiento.csv:** Archivo con el análisis de sentimientos basado en las reseñas, incluyendo puntuaciones de polaridad y palabras clave extraídas. (Ajustar según los análisis de sentimiento realizados).

    * **📄 model_results.csv:** Resultados de las métricas de evaluación de los modelos utilizados (precisión, recall, F1-score, etc.).

* **📄 data_description.md:** Descripción del contenido de los datos.