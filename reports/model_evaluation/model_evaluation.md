<div style="text-align: center;">
<image src="docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# 🔎 Evaluación de Modelos

## 📌 Descripción

Este documento presenta las métricas de desempeño de los modelos utilizados en el análisis de percepción de usuarios en Booking, así como un análisis comparativo entre ellos.

## 📊 Pruebas y Validaciones Realizadas

Se realizaron diversas pruebas para evaluar la efectividad de los modelos aplicados en el análisis de las reseñas de Booking:

- **Preprocesamiento de texto:** Eliminación de stopwords, tokenización y vectorización de texto con TF-IDF.
- **Entrenamiento de modelos:** Se entrenaron modelos no supervisados (K-Means) para clustering y modelos supervisados (Naïve Bayes, Random Forest, XGBoost y LSTM) para clasificación de sentimiento.
- **Evaluación de modelos:** Se utilizaron métricas como accuracy, F1-score y recall para los modelos supervisados.

## 🏆 Resultados de los Modelos

### Modelos Supervisados

| Modelo | Accuracy | F1-score | Recall | Precision | Tiempo Entrenamiento (s) | Tiempo Predicción (s) |
|---|---|---|---|---|---|---|
| Naïve Bayes | 0.3731 | 0.2663 | 0.3731 | 0.3338 | 0.0281 | 0.0020 |
| Random Forest | 0.3786 | 0.2438 | 0.3786 | 0.5112 | 71.3783 | 0.2364 |
| XGBoost | 0.3810 | 0.2668 | 0.3810 | 0.3922 | 49.1133 | 0.0906 |

**Observación:** Se omitió el modelo LSTM debido a que no proporcionó valores para F1-score y Recall.

### Modelo No Supervisado (K-Means)

Puntuación Silhouette Score: 0.386073236409909

Los resultados del clustering se guardaron en `models/kmeans_model.pkl`.

## ⚖️ Comparación entre Modelos y Justificación de Elección

Los modelos supervisados mostraron un rendimiento similar en la predicción de la satisfacción del usuario.  El modelo XGBoost tuvo el mejor desempeño en términos de accuracy, F1-score y recall.

El modelo K-Means permitió agrupar las reseñas en clusters basados en similitudes en el texto. Esto puede ser útil para identificar diferentes temas y patrones en las reseñas.

## 📌 Modelo Seleccionado

Se seleccionó el modelo **XGBoost** como el mejor modelo para la clasificación de sentimiento debido a su mejor desempeño en las métricas de evaluación.

## ⚠️ Limitaciones

* La columna "Calificación" solo contiene el valor 10, lo que puede haber afectado el rendimiento de los modelos supervisados.
* El modelo LSTM no proporcionó valores para F1-score y Recall.
* El puntaje Silhouette Score para el modelo K-Means indica que los clusters tienen cierta superposición.
* Las métricas se guardaron en `data/results/model_results.csv`.

## 📂 Documentos Relacionados

- 🔗 [Evaluación de Calidad de Datos](../data_quality/data_quality.md)
- 🔗 [Validación de Datos](../data_quality/data_validation.md)
- 🔗 [Gestión y Planificación](../../project_management/booking_perception_project_plan.md)