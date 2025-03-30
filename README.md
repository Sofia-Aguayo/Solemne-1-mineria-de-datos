Análisis e interpretación de los resultados

Los gráficos generados permiten analizar y comparar datos de temperatura y precipitación provenientes de 2 fuentes distintas: BigQuery (NOAA GSOD) y NASA (T2M). Es evidente que existe una diferencia significativa entre ambas series de datos, lo que puede deberse a diferencia de métodos de recolección o interpolación de datos entre las 2 fuentes.

A continuación explico los gráficos generados:

1. Gráfico comparativo de temperaturas de las 2 fuentes:
   Este gráfico muestra las temperaturas diarias registradas en Santiago durante enero de 2022 por las 2 fuentes ya mencionadas. Es evidente que existe una diferencia significativa entre ambas series de datos, puede ser por los métodos de recolección o interpolación de los datos.

2. Precipitación diaria (NASA):
   Este gráfico de barras muestra la precipitación total diaria medida por la NASA durante enero 2022. Se observa que hay dias específicos con precipitaciones considerables, mientras que la mayoría de días no se detecta precipitación. Y esto es consistente poeque el clima generalmente es seco en Santiago durante el verano.
   
3. Gráfico combinado de temperatura y precipitación
   En este gráfico combino 2 variables: temperatura (línea roja) y precipitación (barras). Permite analizar si existe alguna relación entre la precipitación y las temperaturas diarias considerando que la temperatura disminuye cuando se producen precipitaciones, lo cual es el comportamiento esperado.

4. Matriz de correlación:
  Este mapa de calor muestra la correlación entre las variables de la temperatura de BigQuery, Nasa y la precipitación medida por la NASA. La correlación negativa entre BigQuery y NASA sugiere que ambas fuentes miden temperaturas de manera distinta. Por otro lado, la correlación entre temperatura y precipitación es baja, lo cual sugiere que no existe una relación lineal fuerte entre ambas variables en este periódo.

5. Diferencia de temperaturas (BigQuery vs NASA)
   Este gráfico muestra la diferencia diaria entre las temperaturas medidas por BigQuery y NASA. Permite visualizar de manera clara cómo varía la diferencia entre ambas fuentes a lo largo del mes. Este análisis es util para determinar si existe algún sesgo sistemático o si las diferencias son consistentes.

Se eligeron datos de la NASA porque me llamaba la atención trabajar con datos climáticos debido a mi formación astronomía y nunca había hecho algo así con este tipo de datos. El análisis permite observar diferencias importates entre las temperatura reportadas por NOAA (BigQuery) y NASA, lo cual sugiere que sería necesario investigar más para entender la causa de estas diferencias en los datos. La correlación baja entre temperatura y precipitación es esperable dado el periódo estudiado (Verano en Santiago), pero sería interesante seguir trabajando con otros periódos quizás más extensos para poder observar dependiendo de la estación del año y así identificar tendencias más claras.

