<div style="text-align: center;">
<image src="../images/encabezado.png" alt="EAN + Booking.com" width="800" height="83">
</div>

#
# 📜 Metodología - Booking Perception

La definición de la metodología se soporta en el alcance y objetivos definidos para este proyecto, teniendo en cuenta la fuente de datos de la plataforma Booking.com que es usada para el proyecto, y que su contenido se relaciona con la experiencia registrada por sus clientes entre los años 2023 y 2024 frente a los servicios de hospedaje que fueron contratados, experiencia que es representada en un conjunto de variables que son el objeto de análisis del proyecto.

En atención a lo antes descrito, es importante destacar que el proceso de extraer conocimiento de valor a grandes volúmenes de datos representa una ventaja competitiva que las empresas identifican como un activo de alto valor estratégico que les permite ser cada vez más competitivos en un mercado de dinámico y en donde las experiencias de los clientes son fundamentales para su crecimiento.

Es así como la selección de la metodología adecuada para este proyecto, se sustenta en la capacidad de gestionar procesos de extracción de conocimiento de una fuente específica de datos y una posterior presentación efectiva de estos resultados los cuales pueden ser operacionalizados por el interesado.

Para esta selección se realiza un conjunto de procesos comparativos entre metodologías que de acuerdo al tipo de fuente de datos y el objetivo de análisis pueden entregar un ciclo de vida eficiente para el proyecto a desarrollar:

## Comparación de Metodologías
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-7btt">Metodología</th>
    <th class="tg-7btt">Fases/Etapas</th>
    <th class="tg-7btt">Ventajas</th>
    <th class="tg-7btt">Desventajas</th>
    <th class="tg-7btt">Adecuación al Proyecto</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-fymr">CRISP-DM (Cross Industry Standard Process for Data Mining)</td>
    <td class="tg-0pky">Comprensión del negocio, Comprensión de los datos, Preparación de datos, Modelado, Evaluación, Despliegue</td>
    <td class="tg-0pky">Estructura clara y adaptable, Enfocada en el negocio, Documentación detallada</td>
    <td class="tg-0pky">Puede ser riguroso y menos flexible en iteraciones</td>
    <td class="tg-0pky">Se adapta bien al proyecto porque enfatiza la comprensión del negocio y el despliegue de resultados</td>
  </tr>
  <tr>
    <td class="tg-fymr">KDD (Knowledge Discovery in Databases)</td>
    <td class="tg-0pky">Selección, Preprocesamiento, Transformación, Minado de datos, Interpretación/Evaluación</td>
    <td class="tg-0pky">Centrado en la extracción de conocimiento, Enfatiza la interpretación de patrones</td>
    <td class="tg-0pky">Puede ser técnicamente complejo sin foco en la aplicabilidad empresarial</td>
    <td class="tg-0pky">Es útil para identificar patrones en los datos de clientes</td>
  </tr>
  <tr>
    <td class="tg-fymr">TDSP (Team Data Science Process)</td>
    <td class="tg-0pky">Iniciación del proyecto, Adquisición y exploración de datos, Modelado, Implementación, Monitoreo</td>
    <td class="tg-0pky">Fomenta el trabajo en equipo, Basado en ciclos iterativos, Integración con herramientas de Microsoft</td>
    <td class="tg-0pky">Requiere un equipo experimentado y herramientas específicas</td>
    <td class="tg-0pky">Compatible con Power BI, pero puede ser complejo</td>
  </tr>
  <tr>
    <td class="tg-fymr">OSEMN (Obtaining, Scrubbing, Exploring, Modeling, Interpreting)</td>
    <td class="tg-0pky">Obtención de datos, Limpieza, Exploración, Modelado, Interpretación</td>
    <td class="tg-0pky">Flexible, Centrado en la limpieza de datos</td>
    <td class="tg-0pky">No es un marco formal, Falta de documentación estructurada</td>
    <td class="tg-0pky">Puede ser útil, pero no asegura una gestión estructurada del proyecto</td>
  </tr>
  <tr>
    <td class="tg-fymr">ASUM-DM (Analytics Solutions Unified Method for Data Mining)</td>
    <td class="tg-0pky">Definición, Exploración, Modelado, Implementación, Medición</td>
    <td class="tg-0pky">Orientado a proyectos analíticos empresariales, Buen soporte de IBM</td>
    <td class="tg-0pky">Menos adoptado en la industria, Dependencia de IBM</td>
    <td class="tg-0pky">Puede ser útil, pero menos flexible</td>
  </tr>
</tbody></table>

Fuente: Generado con ChatGPT (OpenAI, 2025).

## Valoración por Enfoque

Teniendo en cuenta las características del proyecto, se contemplaron dos (2) metodologías como las que se acercaban más a los objetivos trazados (KDD (Knowledge Discovery in Databases) y CRISP-DM (Cross Industry Standard Process for Data Mining)), para lo cual se realizó una valoración por enfoque el cual se presenta a continuación:

### Enfoque técnico vs. enfoque empresarial

- KDD se centra en la minería de datos y la interpretación de patrones, pero no tiene una fase clara de comprensión del negocio ni de despliegue de resultados para la toma de decisiones. CRISP-DM, en cambio, prioriza la alineación con los objetivos empresariales desde el inicio y finaliza con una fase de despliegue que facilita la implementación de hallazgos en herramientas de visualización de datos.

- KDD tiene una estructura más técnica y lineal, enfocada en la transformación de datos y modelos analíticos. Por otra parte CRISP-DM es iterativa y flexible, lo que permite adaptarse mejor a cambios en los requerimientos del negocio.

- En este caso, el proyecto busca no solo descubrir patrones en los datos registrados por los clientes, sino también mejorar los servicios y facilitar la toma de decisiones en la empresa, en tal sentido CRISP-DM, al incluir evaluación de modelos y despliegue, garantiza que los resultados sean accionables, mientras que KDD se enfoca más en el análisis sin proporcionar directrices claras para la implementación empresarial.

- Si se considera que la minería de datos es la prioridad absoluta y no tanto la integración de resultados en el negocio, KDD podría ser una opción válida. Sin embargo, dado el objetivo de presentar hallazgos en una herramienta de visualización de datos para la toma de decisiones, CRISP-DM resulta ser la más adecuada.

## Selección de la Metodología
<p align="justify">Teniendo presente las consideraciones realizadas con anterioridad, identificando que para el proyecto se requiere un análisis profundo de la información registrada, identificación de patrones y presentación de resultados en una herramienta especializada de visualización de datos, la metodología que mejor se ajusta a esta necesidad es CRISP-DM (Cross Industry Standard Process for Data Mining).</p>

## CRISP-DM (Cross Industry Standard Process for Data Mining)

La metodología CRISP-DM (Cross Industry Standard Process for Data Mining) es un modelo de proceso estándar ampliamente utilizado en la minería de datos y el análisis de datos. CRISP-DM ofrece una estructura para abordar proyectos de minería de datos de manera organizada y eficiente, cubriendo desde la comprensión del negocio hasta la implementación de soluciones. Fue desarrollada en 1996 por un consorcio de empresas con el objetivo de proporcionar un enfoque estructurado y práctico para proyectos de ciencia de datos, consta de seis fases principales y se contemplan unas subfases que facilitan su ejecución.
<div style="text-align: center;">
<image src="../images/CRISP-DM.jpg" alt="Metodología CRISP-DM" width="400" height="383" align="center">
</div>
<b>1. Comprensión del negocio,</b> en esta fase, el objetivo es comprender los requisitos y objetivos del negocio para traducirlos en una tarea de minería de datos. Se busca responder a preguntas como: ¿Qué problema debe resolverse? ¿Cuáles son los resultados esperados?, subfases (Establecer los objetivos del negocio, evaluar la situación actual y determinar los objetivos del análisis).

<b>2. Comprensión de los datos,</b> implica recopilar los datos disponibles y realizar un análisis inicial para familiarizarse con ellos. Se identifican problemas potenciales, se exploran patrones y se determina la calidad de los datos, subfases (Recolección de datos, descripción y exploración de los datos, verificación de la calidad de los datos).

<b>3. Preparación de los datos,</b> se procesan los datos de forma que sean aptos para la fase de modelado. Esto incluye la limpieza de datos, la selección de variables relevantes, la transformación de variables y la creación de subconjuntos de datos si es necesario, subfases (Selección de los datos relevantes, limpieza de los datos, construcción de nuevas variables o formatos, integración de datos de diferentes fuentes).

<b>4. Modelado,</b> en esta fase se seleccionan y aplican los algoritmos de modelado más adecuados. Dependiendo de los objetivos del proyecto, se pueden utilizar técnicas como la clasificación, la regresión o el agrupamiento. A menudo, esta fase implica un ciclo de prueba y error para ajustar los parámetros de los modelos, subfases (Selección del algoritmo de modelado, construcción del modelo, evaluación del modelo y ajuste de parámetros).

<b>5. Evaluación,</b> aquí, los modelos generados se evalúan a fondo para asegurarse de que son efectivos y responden a los objetivos planteados en la fase de comprensión del negocio. Se considera tanto el rendimiento técnico del modelo como su aplicabilidad a los objetivos del negocio, subfases (Evaluación de la calidad del modelo, validación con criterios del negocio, determinación de los próximos pasos).

<b>6. Despliegue,</b> los resultados se integran en el sistema o proceso de toma de decisiones del negocio. Esto puede implicar la creación de reportes, la implementación de sistemas automatizados o la entrega de insights a los responsables de la toma de decisiones, subfases (Planificación del despliegue, monitoreo y mantenimiento del modelo, documentación del proceso, revisión final y conclusiones del proyecto).

Referencia: Díaz, J. (2024, octubre 20). Comparativa de metodologías minería de datos: KDD, CRISP-DM y SEMMA explicadas. W3PDS. https://es.linkedin.com/pulse/comparativa-de-metodolog%C3%ADas-miner%C3%ADa-datos-kdd-crisp-dm-y-semma-explicadas-3uhwe