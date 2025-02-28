<div style="text-align: center;">
<image src="../images/encabezado.png" alt="EAN + Booking.com" width="800" height="83">
</div>

#
# 🏗️  Arquitectura y Flujos de Procesamiento de Datos

## 📥 Ingesta y Transformación de Datos

1. **Carga de Datos Crudos:**

    * Se reciben datos desde archivos CSV (`reviews_booking.csv`).
    * Se almacenan en el directorio `data/raw/`.

2. **Limpieza y Transformación:**

    * Se elimina la columna 'Unnamed: 0'.
    * Se eliminan valores duplicados.
    * Se convierte la columna 'Calificación' a formato numérico.
    * Se eliminan filas con valores nulos en la columna 'Calificación'.
    * Se crea la columna 'Etiqueta' para análisis de sentimiento.
    * Se imputan valores nulos en campos de texto con 'No especificado'.
    * Se crea la columna "Opiniones" con la concatenación de las columnas "Cosas Positivas" y "Cosas Negativas".
    * Se almacena el resultado en `data/processed/cleaned_data.csv`.

3. **Vectorización de Datos:**

    * Se vectorizan las columnas de texto relevantes utilizando TF-IDF.
    * Los modelos de vectorización se guardan en `models/vectorizer.pkl`

## 🗄️ Almacenamiento y Disponibilidad

* **Datos en diferentes etapas:**

    * Datos crudos en `data/raw/`.
    * Datos procesados en `data/processed/`.
    * Resultados de análisis y modelos en `data/results/` y `models/`.

* **Disponibilidad:**

    * Los datos procesados y resultados son accesibles para análisis y visualizaciones.
    * Se generan archivos CSV y modelos serializados (`.pkl`, `.gz`) para análisis y reporting.

## 📊 Plan de Monitoreo del Pipeline

1. **Registro de Errores:**

    * Se implementan registros (logs) para capturar errores en la ingesta y transformación.

2. **Monitoreo de Calidad de Datos:**

    * Verificación de valores nulos, duplicados y tipos de datos.
    * Validación de distribución de calificaciones y análisis de sentimientos.
    * Se generan reportes de calidad de datos en `reports/data_quality/`.

3. **Automatización y Actualización:**

    * Se programan ejecuciones periódicas para actualizar los datos y re-entrenar modelos.
    * Se implementan notificaciones en caso de errores o anomalías detectadas.

4. **Monitoreo de Modelos:**

    * Se registra el rendimiento de los modelos en `data/results/model_results.csv`
    * Se realiza seguimiento de la deriva del modelo (model drift) con el tiempo, según sea necesario.