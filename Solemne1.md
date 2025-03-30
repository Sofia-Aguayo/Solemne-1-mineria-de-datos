# **Solemne 1 Minería de Datos 2025**

## **Análisis del Cambio Climático y Eventos Extremos** 🌍🔥

### **Objetivos**

Se espera que los alumnos muestren conocimiento en:  

- Consultas a bases de datos públicas en **Google Cloud Platform (BigQuery)**.
- Consumo y procesamiento de datos desde **APIs climáticas**.  
- Trabajo con datos en formatos **JSON y relacionales**.  
- Limpieza, transformación y combinación de datos.  
- **Visualización geoespacial y temporal** de tendencias climáticas.  
- Interpretación y narración de hallazgos.  
- Versionado de software y colaboración en GitHub.  

### **Instrucciones**  

Usando datos climáticos públicos de BigQuery y APIs relevantes, se pide realizar lo siguiente:  

1. **Exploración de Datos**  
   - Identificar un **dataset de cambio climático** en **BigQuery** (Ej.: temperaturas globales, emisiones de CO₂, incendios forestales).  
   - Seleccionar una **API pública** para obtener datos en tiempo real o históricos (Ej.: NASA, OpenWeather, Copernicus, NOAA).  
   - Extraer datos relevantes sobre temperaturas, precipitaciones, incendios, o eventos climáticos extremos.  

2. **Limpieza y Transformación de Datos**  
   - Cargar los datos obtenidos en **Pandas**.  
   - Normalizar y combinar los datos de **BigQuery y API**.  
   - Aplicar filtros temporales y espaciales para definir un área/tiempo de estudio.  

3. **Visualización de Datos**  
   - Crear al menos **5 visualizaciones** (gráficos de líneas, mapas de calor, tendencias de temperatura, etc.).  
   - Usar **Matplotlib, Seaborn, Folium o GeoPandas** para representar datos espaciales.  
   - Las visualizaciones deben estar bien etiquetadas, con títulos, ejes y leyendas claras.  

4. **Análisis e Interpretación de Resultados**  
   - Identificar tendencias de cambio climático y correlaciones en los datos.  
   - Comparar registros históricos con valores recientes.  
   - Proporcionar explicaciones claras sobre los insights obtenidos.  

5. **Entrega y Documentación**  
   - Crear un **repositorio en GitHub** para el proyecto.  
   - **Versionar código** usando una rama de desarrollo y otra de producción.  
   <!-- - Incluir un **informe en Markdown o Jupyter Notebook** con los resultados.   -->
   - Adjuntar un archivo `requirements.txt` con las librerías usadas.  
   - Escribir un **README.md** explicando los hallazgos y conclusiones.  

---

### **Fuentes de Datos**  

📊 **BigQuery (Google Cloud Public Datasets)**  

- [NOAA Global Surface Summary of the Day](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2snoaa_gsod) → Temperaturas, humedad, precipitaciones.  
- [OpenAQ Air Quality](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sopenaq) → Contaminación del aire.  
<!-- - [NASA NEX-GDDP](https://console.cloud.google.com/marketplace/details/nasa-public/nex-gddp) → Proyecciones de temperatura global.   -->

🌍 **APIs públicas**  

- [NASA Power](https://power.larc.nasa.gov/) → Datos históricos y pronósticos meteorológicos.  
- [OpenWeather](https://openweathermap.org/api) → Temperaturas y clima actual/histórico.  
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/) → Datos de cambio climático global.  
<!-- - [NOAA Climate API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) → Datos meteorológicos históricos.   -->

---

### **Evaluación**  

| Criterio                              | Puntos |
|---------------------------------------|--------|
| Calidad del análisis y uso de datos   | 2      |
| Claridad y efectividad de visualizaciones | 2  |
| Interpretación y narración de hallazgos | 1  |
| Uso adecuado de GitHub y versionado   | 1      |
| Documentación y presentación de resultados | 1  |
| **Puntaje total**                     | **7**  |
