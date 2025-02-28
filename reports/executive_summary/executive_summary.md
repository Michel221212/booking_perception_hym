<div style="text-align: center;">
<image src="docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# 📊 Resumen Ejecutivo

## 📌 Descripción

Este documento resume los hallazgos clave del proyecto, las métricas principales y las conclusiones más relevantes. Su propósito es proporcionar información clara y concisa para la toma de decisiones estratégicas sobre la percepción de los usuarios en la plataforma Booking.

## 🔍 Hallazgos Clave

* Se identificaron patrones en las valoraciones de usuarios según el tipo de grupo de viaje, aunque las calificaciones promedio fueron consistentemente altas (10) en todos los grupos, lo que sugiere un posible sesgo en la recolección de datos.
* La categoría "Acomodación" presenta un alto porcentaje de datos faltantes (alrededor del 95%), lo que limita el análisis de esta variable.
* Se observaron tendencias recurrentes en aspectos positivos y negativos:
    * **Aspectos positivos más mencionados:** "atención", "ubicación", "hotel", "desayuno", "habitación", "limpieza", "comodidad".
    * **Aspectos negativos más mencionados:** "habitación", "desayuno", "atención", "hotel", "ubicación", "baño", "agua", "ruido".
* Se encontró un sesgo en la distribución de nacionalidad de los usuarios, predominando los de Colombia (171,780 registros).
* Tras la limpieza de datos, se observaron 236,637 valores nulos en la columna "Calificación".

## 📈 Métricas Principales

* Cantidad de reseñas analizadas: 374,604 registros después del preprocesamiento.
* Distribución geográfica: Predominio de reseñas de Colombia (171,780 registros).
* Se eliminó el 14.52% de los datos debido a duplicados o inconsistencias.

## 🚀 Recomendaciones Estratégicas

1. **Mejorar la calidad de los datos:**
    * Implementar medidas para reducir la cantidad de valores nulos en la categoría "Acomodación", ya sea mediante la imputación de valores o la redefinición de la variable.
    * Investigar el posible sesgo en las calificaciones y considerar la posibilidad de recopilar datos de calificación de forma más objetiva.
    * Investigar y abordar la causa de los valores nulos en la columna "Calificación".

2. **Profundizar el análisis de sentimiento:**
    * Analizar con mayor profundidad las palabras clave más frecuentes en los comentarios positivos y negativos para cada grupo de viaje, con el fin de identificar áreas de mejora específicas para cada segmento.

3. **Desarrollar un tablero de visualización:**
    * Crear un dashboard interactivo en Power BI para visualizar los datos y los resultados del análisis de manera más intuitiva y accesible.

4. **Diversificar la muestra:**
    * Ampliar la muestra de usuarios para incluir un mayor número de nacionalidades y obtener una visión global más equilibrada.

## 📂 Documentos Relacionados

- 🔗 [Evaluación de Calidad de Datos](../data_quality/data_quality.md)
- 🔗 [Validación de Datos](../data_quality/data_validation.md)
- 🔗 [Evaluación del Modelo](../model_evaluation/model_evaluation.md)
- 🔗 [Gestión y Planificación](../../project_management/booking_perception_project_plan.md)

## 📌 Conclusión

El análisis de percepciones en Booking ha revelado información valiosa para la optimización de servicios, a pesar de las limitaciones en la calidad de los datos. Se recomienda a los tomadores de decisiones considerar estos hallazgos para mejorar la calidad de la experiencia del usuario, fortalecer la confiabilidad del sistema de valoración y continuar con la optimización del proceso de recolección de datos.