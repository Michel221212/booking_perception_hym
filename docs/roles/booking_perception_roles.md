<div style="text-align: center;">
<image src="../images/encabezado.png" alt="EAN + Booking.com" width="800" height="83">
</div>

#
# 👨‍💻 Definición de Roles
## Descripción
Lista los roles dentro del equipo y sus responsabilidades.

**Data Scientist (con funciones de Project Management)**:
- Preparación de Datos:
Implementar las estrategias de limpieza y preprocesamiento de datos definidas por el Analista de Datos.
Realizar la ingeniería de características (feature engineering) para crear nuevas variables que mejoren el rendimiento de los modelos.
Responsable de modelado, análisis avanzado y extracción de insights.

- Modelado:
Seleccionar los modelos de análisis de sentimiento más adecuados para el proyecto (por ejemplo, modelos basados en lexicones, modelos de machine learning supervisados, modelos de deep learning).
Entrenar, validar y optimizar los modelos utilizando técnicas de machine learning.
Evaluar el rendimiento de los modelos utilizando métricas apropiadas (precisión, recall, F1-score, etc.).

- Evaluación:
Interpretar los resultados del análisis de sentimiento y generar insights accionables para el negocio.
Evaluar el impacto de los modelos en los KPIs definidos por el Analista de Datos.

- Project Management:
Planificar y gestionar el cronograma del proyecto.
Asignar tareas a los miembros del equipo.
Gestionar los riesgos y problemas del proyecto.
Facilitar la comunicación entre los miembros del equipo.
Asegurar que el proyecto se alinee con los objetivos del negocio.

  Reportes:
- Reportes de Rendimiento del Modelo: Métricas de precisión, recall, F1-score, AUC, tiempos de entrenamiento, etc., comparando diferentes modelos y versiones. Incluir análisis de las métricas y justificación de la selección del modelo final.
  Audiencia: Data Analyst, Data Engineer, Stakeholders técnicos.
  Frecuencia: Durante el desarrollo del modelo (semanal), al finalizar el modelado, y en el monitoreo continuo del modelo en producción (mensual).
- Reportes de Insights del Modelo: Explicación de cómo el modelo está tomando decisiones, qué características son más importantes, y cómo se relacionan con el sentimiento expresado.
  Audiencia: Data Analyst, Stakeholders del negocio (en formato no técnico).
  Frecuencia: Al finalizar el modelado, y cuando haya cambios significativos en el modelo.
- Reportes de Gestión del Proyecto: Informes de progreso, hitos alcanzados, riesgos y problemas, uso de recursos.
Audiencia: Stakeholders del proyecto, equipo directivo.
Frecuencia: Semanal o quincenal.

**Data Analyst**: 
- Comprensión del Negocio:
Colaborar con los stakeholders para definir los objetivos del negocio y cómo el análisis de sentimiento puede contribuir.
Identificar los grupos de viaje más relevantes para el análisis.
Definir las métricas clave de rendimiento (KPIs) para el proyecto.

- Comprensión de los Datos:
Explorar la base de datos de Booking para comprender la estructura, el contenido y la calidad de los datos.
Identificar las variables relevantes para el análisis de sentimiento (número de noches, país, tipo de alojamiento, fechas de estancia, grupo de viaje, comentarios de los usuarios, etc.).
Realizar análisis exploratorios para identificar patrones y tendencias en los datos.
Evaluar la calidad de los datos y proponer estrategias para la limpieza y el preprocesamiento.

- Preparación de Datos (en colaboración con el Científico de Datos):
Definir los criterios para la limpieza y el preprocesamiento de los datos.
Participar en la selección de las características (features) más relevantes para el modelado.

- Comunicación:
Presentar los hallazgos iniciales del análisis exploratorio al equipo.
Comunicar los requerimientos del negocio al Científico de Datos y al Arquitecto de Datos.

  Reportes:
- Reportes de Análisis Exploratorio de Datos (EDA): Resúmenes de las características de los datos, distribuciones, relaciones entre variables, identificación de outliers, etc. Incluir visualizaciones claras y concisas.
Audiencia: Data Scientist, Data Engineer, Stakeholders del negocio.
Frecuencia: Al inicio del proyecto, al explorar nuevas fuentes de datos, y cuando se requiera una comprensión más profunda de los datos.
- Reportes de Calidad de Datos: Métricas de integridad, completitud, consistencia y validez de los datos. Identificar fuentes de datos problemáticas y proponer soluciones.
Audiencia: Data Scientist, Data Engineer.
Frecuencia: Periódica (mensual), y antes de cualquier modelado.
- Reportes de Requerimientos del Negocio: Documentación clara y concisa de los objetivos del negocio, las preguntas clave a responder, las métricas de éxito, y las restricciones del proyecto.
Audiencia: Data Scientist, Data Engineer, Stakeholders del negocio.
Frecuencia: Al inicio del proyecto, y cuando haya cambios en los objetivos del negocio.

**Data Engineer**:
- Diseño de la Arquitectura de Datos:
Seleccionar las herramientas y tecnologías de datos más adecuadas para el proyecto (por ejemplo, bases de datos, plataformas de procesamiento de datos, herramientas de visualización de datos).
Diseñar la arquitectura de datos para garantizar la escalabilidad, la seguridad y la confiabilidad de los datos.

- Implementación de la Infraestructura de Datos:
Construir las conexiones entre las diferentes fuentes de datos.
Configurar y optimizar las plataformas de procesamiento de datos.
Implementar medidas de seguridad para proteger los datos.

- Despliegue:
Desplegar los modelos de análisis de sentimiento en un entorno de producción.
Monitorear el rendimiento de los modelos y la infraestructura de datos.
Realizar ajustes y optimizaciones según sea necesario.

- Colaboración:
Trabajar en estrecha colaboración con el Científico de Datos para garantizar que la infraestructura de datos satisfaga las necesidades del proyecto.
Brindar soporte técnico a los miembros del equipo.

Reportes:
- Reportes de Infraestructura: Métricas de rendimiento de la infraestructura (latencia, throughput, uso de recursos), estado de los componentes, alertas de errores.
Audiencia: Data Scientist, Data Analyst, Equipo de Operaciones.
Frecuencia: Continua (monitoreo en tiempo real), y reportes agregados diarios/semanales.
- Reportes de Calidad de Datos (Técnico): Monitoreo de la calidad de los datos en la infraestructura (duplicados, datos faltantes, inconsistencias), y cumplimiento de las reglas de calidad de datos.
Audiencia: Data Analyst, Data Scientist.
Frecuencia: Periódica (diaria/semanal), y alertas en tiempo real si se detectan problemas críticos.
- Reportes de Seguridad de Datos: Registros de acceso a los datos, detección de amenazas, cumplimiento de políticas de seguridad, y auditorías de seguridad.
Audiencia: Equipo de Seguridad, Equipo de Cumplimiento.
Frecuencia: Continua (monitoreo en tiempo real), y reportes agregados mensuales/trimestrales.

Puntos clave para evitar la superposición:
-El Data Scientist se enfoca en los reportes relacionados con el rendimiento, la explicación y la gestión del modelo.
-El Data Analyst se enfoca en los reportes relacionados con la calidad de los datos, el análisis exploratorio y los requerimientos del negocio.
-El Data Engineer se enfoca en los reportes relacionados con la infraestructura, la calidad de los datos (desde una perspectiva técnica) y la seguridad de los datos.
