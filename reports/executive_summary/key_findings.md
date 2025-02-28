<div style="text-align: center;">
<image src="docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# 📊 Hallazgos Clave

## Descripción

Este documento resume los descubrimientos más relevantes obtenidos durante el análisis de datos.

## 🔍 Principales Insights Identificados

1. **Sesgo en las Calificaciones:**

* Se identificó que todas las calificaciones son 10, lo que indica un fuerte sesgo en la recolección de datos o en la forma en que los usuarios califican las experiencias.
* Esto limita la posibilidad de realizar análisis más profundos sobre la satisfacción del cliente en función de la calificación.

2. **Relación entre la Satisfacción y las Variables Textuales:**

* Se analizaron las palabras clave más frecuentes en las columnas "Cosas Positivas" y "Cosas Negativas" para cada grupo de viaje.
* Algunas de las palabras más comunes son:
    * **Positivas:** "atención", "ubicación", "hotel", "desayuno", "habitación", "limpieza", "comodidad".
    * **Negativas:** "habitación", "desayuno", "atención", "hotel", "ubicación", "baño", "agua", "ruido".
* Este análisis proporciona información valiosa sobre los aspectos que los usuarios valoran más y aquellos que necesitan mejoras.

3. **Problemas de Calidad de Datos:**

* Se detectó una cantidad significativa de valores nulos en la columna "Acomodación" (95% de datos faltantes).
* La limpieza de datos redujo el conjunto de datos de 438,213 filas a 374,604 filas, eliminando filas duplicadas.
* Se encontraron 236,637 valores nulos en la columna "Calificación" después de la limpieza.

4. **Distribución de Nacionalidad de los Usuarios:**

* Predomina la nacionalidad "Colombia" (171,780 registros), lo que sugiere una tendencia hacia el mercado local.
* Podría ser necesario diversificar la muestra para obtener una visión global más equilibrada.

5. **Relación entre Tipo de Viaje y Satisfacción:**

* Se analizaron las calificaciones promedio para cada grupo de viaje ("En familia", "En grupo", "En pareja", "Persona que viaja sola").
* No se observaron diferencias significativas en las calificaciones entre los diferentes grupos de viaje, lo que indica que la satisfacción general es alta en todos los segmentos.

## 📌 Impacto de los Hallazgos en la Toma de Decisiones

* **Estrategias de Mejora:** Se recomienda enfocar las estrategias en los aspectos negativos más recurrentes (mencionados en el punto 2) para mejorar la experiencia del usuario.
* **Optimización del Proceso de Evaluación:** Se deben establecer mecanismos para reducir el sesgo en las calificaciones, como encuestas más detalladas o preguntas abiertas.
* **Manejo de Datos Faltantes:** Dado el alto porcentaje de valores nulos en "Acomodación", se recomienda evaluar la necesidad de esta variable o buscar fuentes adicionales para completar la información.
* **Manejo de Datos Faltantes en Calificación:** Se debe investigar la causa de los valores nulos en "Calificación" y determinar si es necesario imputar o eliminar estos registros.

## 📊 Comparación con los Objetivos Iniciales

| **Objetivo Inicial** | **Resultado** |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| Identificar patrones en las reseñas | Se detectaron palabras clave en las opiniones positivas y negativas para cada grupo de viaje. |
| Evaluar la fiabilidad de las calificaciones | Se identificó un sesgo en las calificaciones con tendencia a la puntuación máxima (10) y una gran cantidad de valores nulos después de la limpieza. |
| Determinar qué servicios necesitan mejoras | Se identificaron los problemas recurrentes mencionados en el punto 2. |
| Evaluar la calidad del dataset | Se identificaron valores nulos, sesgo en la nacionalidad de los usuarios y problemas con la columna "Calificación". |

## 📂 Documentos Relacionados

* 🔗 [Evaluación de Calidad de Datos](../data_quality/data_quality.md)
* 🔗 [Validación de Datos](../data_quality/data_validation.md)
* 🔗 [Evaluación del Modelo](../model_evaluation/model_evaluation.md)
* 🔗 [Gestión y Planificación](../../project_management/booking_perception_project_plan.md)
