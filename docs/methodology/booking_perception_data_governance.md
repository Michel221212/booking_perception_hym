<div style="text-align: center;">
<image src="../images/encabezado.png" alt="EAN + Booking.com" width="800" height="83">
</div>

#
# 📜 Gobernanza de Datos

Este documento detalla las políticas de gobernanza de datos implementadas en el proyecto, asegurando la calidad, privacidad y seguridad de la información utilizada para el análisis de reseñas hoteleras.

## 📌 Normas y Estándares Aplicados

1. **Normativas Internacionales:** Se siguen principios de buenas prácticas en gestión de datos, alineados con ISO 27001 (Seguridad de la Información) y ISO 9001 (Calidad de Datos).

2. **Estandarización de Datos:**

    * Uso de formatos consistentes para almacenamiento (`.csv`, `.md`, `.pkl`, `.gz`).
    * Normalización de variables categóricas y textuales.
    * Aplicación de encoding en variables categóricas para análisis avanzado (usando `label_encoder.pkl`).

3. **Calidad de Datos:**

    * Eliminación de registros duplicados.
    * Tratamiento de valores nulos mediante eliminación o imputación, según la variable.
    * Validación de datos numéricos y categóricos.
    * Generación de reportes de calidad de datos en `reports/data_quality/`.

## 🔒 Privacidad y Seguridad de Datos

1. **Anonimización y Protección de Datos Sensibles:**

    * Eliminación de identificadores personales en las reseñas.
    * Uso de técnicas de agregación para evitar exposición de información individual.

2. **Control de Acceso:**

    * Restricción de acceso a los datos crudos a personal autorizado.
    * Implementación de roles y permisos en el almacenamiento de datos.
    * Uso de `.gitignore` para prevenir la inclusión de datos sensibles en el control de versiones.

3. **Almacenamiento Seguro:**

    * Resguardo de datos en directorios protegidos (`data/raw`, `data/processed`, `models`).
    * Copias de seguridad periódicas para prevención de pérdida de información.

4. **Cumplimiento de Regulaciones:**

    * Adherencia a normativas de protección de datos como el GDPR y la Ley de Habeas Data.

## 🛠️ Control y Auditoría de Datos

1. **Registro de Cambios:**

    * Documentación de transformaciones aplicadas en `data/processed/cleaned_data.csv`.
    * Registro de versiones y modificaciones en `data/results/data_description.md`.
    * Uso de registros (logs) para capturar errores en la ingesta y transformación.

2. **Monitoreo de Calidad:**

    * Verificación de consistencia en formatos y valores.
    * Validación de métricas estadísticas en `data/results/analisis_general.csv` y `data/results/analisis_por_grupo.csv`.
    * Monitoreo del rendimiento de modelos y deriva de modelos, según sea necesario.

3. **Trazabilidad de Datos:**

    * Mapeo del flujo de datos desde la ingesta hasta la generación de resultados.
    * Uso de logs para seguimiento de procesamiento y análisis.
    * Documentación del pipeline de datos en `docs/methodology/booking_perception_data_pipeline_design.md`.

### 📌 Estas políticas garantizan la integridad, seguridad y calidad de los datos utilizados en el proyecto.