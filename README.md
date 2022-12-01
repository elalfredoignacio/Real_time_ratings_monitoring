# Real_time_ratings_monitoring
Arquitectura pipeline para streaming de tiempo real

El procesamiento de streaming de datos en tiempo real o casi tiempo real (near real time), permite obtener insights en el mismo momento en que están arribando, lo que posibilita tomar decisiones rápidamente a partir del objetivo definido. El uso de un sistema distribuido de procesamiento es clave en aplicaciones de Big Data dados por la variabilidad, velocidad de generación, y grandes volúmenes de datos (las 3 “V” de Big Data).
El presente proyecto pretende implementar una solución para monitorear en tiempo real el rating promedio de distintos productos comercializados por la plataforma de e-commerce de Amazon. Se describe la implementación de un sistema de streaming basado en una arquitectura de referencia para IoT, utilizando un Broker MQTT para IoT como es Mosquitto, y herramientas de software libre dentro del ecosistema Apache.
A los efectos del caso de uso seleccionado, los datos provienen del dataset de calificaciones de productos en la plataforma e-commerce de Amazon. 
Si bien no se trata de una aplicación que implique la generación de streaming de datos a partir de dispositivos IoT, desde el punto de vista académico el modelo es totalmente válido. La etapa de Edge (fuera del contexto de nuestro sistema), en vez de ser un dispositivo IoT, será un script de Python que simula la generación de los datos de streaming a partir de un archivo csv con los datos de calificaciones de productos de Amazon.

Contenido directorio Anexos:
- Jupyter Notebook con pre-procesamiento de los CSV de ratings originales (preprocesamiento.ipynb)
- Script Python con el generador del stream y Broker Mosquitto (reproductor_ratings.py)
- Template de NiFi con el Process Group que incluye el flujo implementado (Amazon_NiFi.xml) 
- Log de salida de Flink para la categoría Movies and TV (taskmanager_10.0.0).
- Excel con validación de los resultados para los primeros datos del CSV (validación ventanas.xlsx)
- Dashboard en Power BI para los resultados de la categoría Home and Kitchen (visualizacion Home&Kitchen.pbix)
- Dashboard en Tableau para los resultados de la categoría Movies and TV (dashboard_Tableau_1.pdf y dashboard_Tableau_2.pdf).
