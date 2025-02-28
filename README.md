<div style="text-align: center;">
<image src="docs/images/encabezado.png" alt="Descripción de la imagen" width="800" height="83">
</div>

#
# 📖 Proyecto - Booking Perception

## 👥 Equipo de Trabajo
- **✅ Hannan Nayibe Yousef Novoa**
- **✅ Yohn Forthis Hernandez Mendoza**
- **✅ Michel Stivens Larrota Villalba**

## 📌 Descripción General
El proyecto Booking Perception tiene como objetivo analizar las reseñas de usuarios en la plataforma Booking.com para identificar patrones y tendencias en la percepción del servicio. Utilizando la metodología CRISP-DM, se busca extraer información valiosa sobre aspectos positivos y negativos de las experiencias de los viajeros, con el fin de proponer mejoras en la oferta turística.

## 🔄 Flujo del Proyecto (CRISP-DM)
1. **Comprensión del Negocio:** Definir objetivos y preguntas clave.
2. **Comprensión de los Datos:** Exploración, limpieza y estructura del dataset.
3. **Preparación de los Datos:** Transformación, normalización y selección de variables.
4. **Modelado:** Análisis de sentimientos y segmentación de opiniones.
5. **Evaluación:** Validación del modelo y análisis de resultados.
6. **Implementación:** Visualización de datos y despliegue en Power BI.

## 📂 Estructura del Proyecto

### 📁 data
- **processed/**: Contiene los datos procesados y limpios listos para el análisis.
    - `cleaned_data.csv`: Datos preprocesados después de limpieza y transformación.
- **raw/**: Almacena los datos en su formato original sin modificaciones.
    - `reviews_booking.csv`: Reseñas sin procesar obtenidas de la plataforma Booking.com.
- **results/**: Archivos generados después del análisis.
    - `analisis_general.csv`: Resultados del análisis global de las reseñas.
    - `analisis_por_grupo.csv`: Segmentación del análisis por grupos de viaje.
    - `analisis_sentimiento.csv`: Análisis de sentimiento aplicado a las reseñas.
    - `model_results.csv`: Resultados de los modelos aplicados.
- `data_description.md`: Documentación de los datos utilizados en el proyecto.

### 📁 docs
- **images/**: Imágenes para documentar el proyecto.
- **methodology/**: Documentos relacionados con la metodología utilizada.
    - `booking_perception_methodology.md`: Descripción detallada del enfoque CRISP-DM aplicado.
    - `booking_perception_data_governance.md`: Normas y estrategias para la gestión de datos.
    - `booking_perception_data_pipeline_design.md`: Diseño del flujo de datos y transformación.
- **roles/**: Definición de responsabilidades dentro del equipo.
    - `booking_perception_roles.md`: Explicación de los roles asignados en el proyecto.
- **tools_and_environment/**: Herramientas y entornos utilizados.
    - `booking_perception_tools.md`: Software y tecnologías empleadas en el desarrollo.

### 📁 models
- `kmeans_model.pkl`: Modelo K-Means entrenado para segmentación.
- `label_encoder.pkl`: Codificador para transformar variables categóricas.
- `mejor_modelo.gz`: Modelo con mejor rendimiento identificado.
- `vectorizer.pkl`: Modelo de vectorización para el procesamiento de texto.

### 📁 notebooks
- `booking_perception_notebooks_guide.md`: Guía de notebooks con análisis exploratorios y modelos.

### 📁 project_management
- `booking_perception_project_plan.md`: Planificación y cronograma del proyecto.
- `booking_perception_risk_assessment.md`: Evaluación de riesgos y estrategias de mitigación.
- `booking_perception_stakeholder_analysis.md`: Identificación y análisis de partes interesadas.

### 📁 reports
- **data_quality/**: Evaluación de la calidad de los datos.
    - `data_quality.md`: Análisis de calidad de los datos.
    - `data_validation.md`: Proceso de validación de datos.
- **executive_summary/**: Resumen de hallazgos y resultados clave.
    - `executive_summary.md`: Informe ejecutivo del proyecto.
    - `key_findings.md`: Principales hallazgos extraídos del análisis.
- **model_evaluation/**: Evaluación de los modelos aplicados.
    - `model_evaluation.md`: Métricas y desempeño de los modelos entrenados.

### 📁 src
- `analyze_data.py`: Código para el análisis de datos y generación de reportes.
- `booking_perception_code_guidelines.md`: Guía de estilo y buenas prácticas en código.
- `clean_data.py`: Módulo para la limpieza y preprocesamiento de datos.
- `load_data.py`: Función para cargar y estructurar datos en el pipeline.
- `main.py`: Script principal para la ejecución del proyecto.
- `train_models.py`: Código para el entrenamiento de modelos de clasificación y clustering.

### 📌 Archivos adicionales
- `.gitignore`: Archivos y carpetas excluidos del control de versiones.
- `poetry.lock`: Dependencias del entorno gestionadas con Poetry.
- `pyproject.toml`: Configuración del entorno y paquetes de desarrollo.
- `README.md`: Documentación principal del proyecto.

## 📄 Documentación del Proyecto

### 📘 Metodología
- 📖 **Metodología utilizada:** [Metodología CRISP-DM](docs/methodology/booking_perception_methodology.md)
- 🏛 **Gobernanza de Datos:** [Gobernanza de Datos](docs/methodology/booking_perception_data_governance.md)
- 🔀 **Diseño del Flujo de Datos:** [Diseño del Pipeline](docs/methodology/booking_perception_data_pipeline_design.md)

### 🛠 Herramientas y Entorno
- 🛠 **Herramientas utilizadas:** [Herramientas utilizadas](docs/tools_and_environment/booking_perception_tools.md)

### 👥 Gestión del Proyecto
- 📌 **Plan del Proyecto:** [Plan del Proyecto](project_management/booking_perception_project_plan.md)
- ⚠ **Evaluación de Riesgos:** [Evaluación de Riesgos](project_management/booking_perception_risk_assessment.md)
- 🏢 **Análisis de Stakeholders:** [Análisis de Stakeholders](project_management/booking_perception_stakeholder_analysis.md)

### 📊 Reportes y Evaluación
- 📊 **Evaluación de Calidad de Datos:** [Calidad de Datos](reports/data_quality/data_quality.md)
- 📑 **Validación de Datos:** [Validación de Datos](reports/data_quality/data_validation.md)
- 📈 **Evaluación del Modelo:** [Evaluación del Modelo](reports/model_evaluation/model_evaluation.md)
- 📊 **Resumen Ejecutivo:** [Resumen Ejecutivo](reports/executive_summary/executive_summary.md)
- 🔍 **Hallazgos Clave:** [Hallazgos Clave](reports/executive_summary/key_findings.md)

### 📓 Notebooks
- 📄 **Guía de Notebooks:** [Guía de Notebooks](notebooks/booking_perception_notebooks_guide.md)

### 🛠 Herramientas Utilizadas

* **Lenguaje:** Python 3.11.11 🐍
* **IDE:** Visual Studio Code 💻
* **Gestor de Paquetes:** Anaconda 🐍📦
* **Gestión del Proyecto:** Jira 📊
* **Visualización:** Power BI 📊
* **Plataforma de Publicación:** Railway.com 🚀
* **Control de Versiones:** GitHub 🔗

## 📌 Contacto
Si tienes preguntas o sugerencias, contáctanos a través del equipo de trabajo. 📩