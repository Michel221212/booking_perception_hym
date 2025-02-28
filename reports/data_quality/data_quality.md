<div style="text-align: center;">
<image src="../../docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

# 🧹 Calidad de Datos

📌 **Objetivo:**

Este informe analiza la calidad de los datos utilizados en el proyecto de análisis de reseñas de Booking, identificando problemas encontrados y describiendo las estrategias de limpieza implementadas.

🔍 **Problemas Encontrados:**

* 📉 **Valores Nulos:** Se encontraron valores nulos en varias columnas del conjunto de datos. A continuación, se detalla la cantidad de valores nulos antes y después de la limpieza:

    **Antes de la limpieza:**

    | Columna           | Valores Nulos |
    |-------------------|--------------|
    | Unnamed: 0       | 0            |
    | País             | 1972         |
    | Acomodación      | 418310       |
    | Noches           | 0            |
    | Fecha hospedaje  | 0            |
    | Grupo viaje      | 2            |
    | Fecha reseña     | 0            |
    | Titulo           | 661          |
    | Calificación     | 0            |
    | Cosas Positivas  | 201357       |
    | Cosas Negativas  | 258200       |
    | reseña           | 0            |

    **Después de la limpieza:**

    | Columna           | Valores Nulos |
    |-------------------|--------------|
    | País             | 1836         |
    | Acomodación      | 354714       |
    | Noches           | 0            |
    | Fecha hospedaje  | 0            |
    | Grupo viaje      | 2            |
    | Fecha reseña     | 0            |
    | Titulo           | 0            |
    | Calificación     | 236637       |
    | Cosas Positivas  | 0            |
    | Cosas Negativas  | 0            |
    | reseña           | 0            |
    | Etiqueta         | 0            |


* 🔄 **Filas Duplicadas:** Se detectaron y eliminaron 63,609 filas duplicadas para evitar sesgos en el análisis.

🛠️ **Estrategias de Limpieza:**

1. **Eliminación de la columna "Unnamed: 0":** No aportaba información relevante.
2. **Conversión de la columna "Calificación" a tipo numérico:** Para facilitar el análisis.
3. **Eliminación de filas con valores nulos en "Calificación":** Se consideró importante preservar la información de la calificación para el análisis.
4. **Creación de la columna "Etiqueta" basada en la "Calificación":** Para categorizar las reseñas.
5. **Eliminación de filas duplicadas:** Para evitar sesgos.
6. **Relleno de valores nulos en columnas de texto con "No especificado":** Aplicado a "Cosas Positivas", "Cosas Negativas" y "Titulo".
7. **Creación de la columna "Opiniones"**: Combinación de las columnas "Cosas Positivas" y "Cosas Negativas".

📊 **Métricas de Calidad de Datos:**

- Filas con valores nulos en "Calificación": 236,637
- Filas duplicadas eliminadas: 63,609
- Total de filas antes de la limpieza: 438,213
- Total de filas después de la limpieza: 374,604

✅ **Resultados:**

Después de aplicar las estrategias de limpieza, se obtuvo un conjunto de datos con mejor calidad, sin filas duplicadas ni valores nulos en las columnas "Cosas Positivas", "Cosas Negativas" y "Titulo". Se reemplazaron los valores nulos en las columnas de texto con "No especificado" para mantener la integridad de los datos. Sin embargo, persisten valores nulos en "País" y "Acomodación", lo que limita algunos análisis específicos. Además, la columna "Calificación" presenta una gran cantidad de valores nulos luego de la limpieza.

⚠️ **Limitaciones:**

- La eliminación de filas con valores nulos puede resultar en la pérdida de información potencialmente valiosa, en especial la gran cantidad de valores nulos eliminados en "Calificación".
- Persisten valores nulos en ciertas columnas como "País" y "Acomodación".
- La columna "Calificación" solo contiene el valor 10, lo que podría indicar un sesgo en la recolección de datos o un problema en la captura de datos.

🔎 **Recomendaciones:**

- Analizar en mayor profundidad los valores nulos restantes para definir mejores estrategias de tratamiento.
- Implementar métodos de validación de datos en la captura de información para reducir errores.
- Monitorear continuamente la calidad de los datos para mantener la integridad del análisis.
- Investigar la causa de los valores nulos en "Calificación" y determinar si es necesario imputar o eliminar estos registros.
- Considerar estrategias para obtener datos de "Acomodación".

📌 **Conclusión:**

La limpieza de datos es un paso crucial en cualquier proyecto de análisis de datos. Las estrategias implementadas en este proyecto permitieron mejorar la calidad del conjunto de datos y obtener resultados más confiables. Sin embargo, es importante seguir mejorando los procesos de limpieza y validación para asegurar la calidad del análisis a largo plazo.