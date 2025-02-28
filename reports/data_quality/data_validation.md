<div style="text-align: center;">
<image src="../../docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# ✅ Validación de Datos

📌 **1. Métodos de Validación Aplicados**

Se aplicaron los siguientes métodos para evaluar la calidad y coherencia de los datos:

* 🔍 **Identificación de valores nulos:** Se evaluó la cantidad de valores faltantes en cada columna antes y después del proceso de limpieza.
* 📊 **Detección de valores atípicos:** Se analizaron distribuciones de datos categóricos y numéricos.
* ⏳ **Verificación de coherencia temporal:** Se revisó que las fechas de reseña y de hospedaje sean lógicas y no contengan valores fuera de rango.
* 📌 **Consistencia de datos categóricos:** Se verificó la uniformidad en nombres de categorías como "Grupo viaje".
* 📈 **Análisis de frecuencias:** Se revisaron los valores más comunes en variables textuales como "Cosas Positivas" y "Cosas Negativas".

⚠️ **2. Errores Detectados y Correcciones Implementadas**

🔴 **Antes de la limpieza:**

| 📂 Columna | ❌ Valores Nulos |
|---|---|
| Unnamed: 0 | 0 |
| País | 1972 |
| Acomodación | 418310 |
| Noches | 0 |
| Fecha hospedaje | 0 |
| Grupo viaje | 2 |
| Fecha reseña | 0 |
| Titulo | 661 |
| Calificación | 0 |
| Cosas Positivas | 201357 |
| Cosas Negativas | 258200 |
| reseña | 0 |

🛑 **Problemas detectados:**

* 📌 **"Acomodación"** tenía más de 418,000 valores nulos (95% de la columna).
* 📉 **"Cosas Positivas"** y **"Cosas Negativas"** con más de 200,000 valores nulos, afectando el análisis de sentimiento.
* 📝 **"Titulo"** con 661 valores nulos, indicando reseñas incompletas.
* 🗑️ Se eliminó la columna "Unnamed: 0" por no ser relevante.

🟢 **Después de la limpieza:**

| 📂 Columna | ✅ Valores Nulos |
|---|---|
| País | 1836 |
| Acomodación | 354714 |
| Noches | 0 |
| Fecha hospedaje | 0 |
| Grupo viaje | 2 |
| Fecha reseña | 0 |
| Titulo | 0 |
| Calificación | 236637 |
| Cosas Positivas | 0 |
| Cosas Negativas | 0 |
| reseña | 0 |
| Etiqueta | 0 |

✅ **Correcciones implementadas:**

* 🗑️ Se eliminaron 63,609 filas duplicadas.
* 🗑️ Se eliminaron 236,637 filas con valores nulos en "Calificación".
* 📊 Reducción del dataset de 438,213 filas a 374,604 filas (-14.52%).
* 🔄 Se convirtió la columna "Calificación" a numérica.
* ✍️ Se imputaron valores en columnas textuales clave ("Cosas Positivas", "Cosas Negativas", "Titulo") con "No especificado".
* 📌 Se uniformizaron categorías en "Grupo viaje".
* 🏷️ Se creó la columna "Etiqueta" para categorizar las reseñas.
* 📝 Se creó la columna "Opiniones" combinando "Cosas Positivas" y "Cosas Negativas".

🏆 **3. Evaluación de Calidad y Consistencia**

📊 **Distribución de datos:**

* 🌍 "País" tiene 210 valores únicos, con "Colombia" predominando (171,780 registros).
* 🏨 "Acomodación" sigue teniendo un alto porcentaje de datos faltantes.
* ⭐ "Calificación" muestra una media de 10 en todas las categorías de "Grupo viaje".

💬 **Análisis de sentimientos:**

* ✅ Se realizó el análisis de sentimiento con las columnas "Cosas Positivas" y "Cosas Negativas", identificando las palabras clave más frecuentes para cada grupo de viaje.

📌 **Conclusiones:**

* 🔄 Mejora en la estructura y calidad de los datos eliminando valores nulos, imputando valores faltantes y normalizando categorías.
* ⚠️ "Acomodación" aún presenta muchos valores faltantes, requiriendo estrategias adicionales.
* ⚠️ La columna "Calificación" solo contiene el valor 10, lo que podría indicar un sesgo en la recolección de datos o un problema en la captura de datos.
* ⚠️ La gran cantidad de valores nulos eliminados en "Calificación" impacta la representatividad del análisis.

📁 **Datos limpios y analizados guardados en:**

- 📌 `data/processed/cleaned_data.csv`
- 📌 `data/results/analisis_general.csv`
- 📌 `data/results/analisis_por_grupo.csv`