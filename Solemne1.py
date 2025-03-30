import requests
import pandas as pd
from google.cloud import bigquery
import matplotlib.pyplot as plt
import seaborn as sns
import folium

#Parte 1...

bq_client = bigquery.Client()

query = """
SELECT
  year,
  mo,
  da,
  temp
FROM
  `bigquery-public-data.noaa_gsod.gsod2022`
WHERE
  stn = '854690' AND year = '2022' AND mo = '01'
"""

df_bq = bq_client.query(query).to_dataframe()

df_bq["fecha"] = pd.to_datetime(
    df_bq["year"].astype(str)
    + df_bq["mo"].astype(str).str.zfill(2)
    + df_bq["da"].astype(str).str.zfill(2),
    format="%Y%m%d"
)

# Convierto los grados a celcius
df_bq["temp_C"] = (df_bq["temp"] - 32) * 5 / 9

# Mostrar tabla
print("\n=== Datos de BigQuery (NOAA GSOD) ===")
print(df_bq.head(10))

class NasaPowerClient:
    def __init__(self, community="RE"):
        self.base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
        self.community = community

    def fetch_dataset(self, latitude, longitude, start, end, parameters):
        url = (
            f"{self.base_url}?start={start}&end={end}"
            f"&latitude={latitude}&longitude={longitude}"
            f"&parameters={parameters}"
            f"&community={self.community}&format=JSON"
        )
        response = requests.get(url)
        return response.json()

# Coordenadas y fechas
lat, lon = -33.45, -70.66
start, end = "20220101", "20220131"
params = "T2M,PRECTOTCORR"

nasa_client = NasaPowerClient()
data = nasa_client.fetch_dataset(lat, lon, start, end, params)

df_nasa = pd.DataFrame({
    "T2M": pd.Series(data["properties"]["parameter"]["T2M"]),
    "PRECTOTCORR": pd.Series(data["properties"]["parameter"]["PRECTOTCORR"])
})
df_nasa.index = pd.to_datetime(df_nasa.index, format="%Y%m%d")


print("\n=== Datos de la API NASA ===")
print(df_nasa.head(10))


# Parte 2

df_bq_grouped = df_bq.groupby("fecha")["temp_C"].mean().reset_index()

df_nasa_grouped = df_nasa.copy()
df_nasa_grouped["fecha"] = df_nasa_grouped.index

merged_df = pd.merge(df_bq_grouped, df_nasa_grouped, on="fecha", how="inner")

merged_df.rename(columns={
    "temp_C": "BigQuery_TEMP_C",
    "T2M": "NASA_T2M_C"
}, inplace=True)

print("\n=== Datos combinados BigQuery + NASA ===")
print(merged_df.head(10))


#Gráfico de comparación de temperaturas
plt.figure(figsize=(10, 5))
plt.plot(merged_df["fecha"], merged_df["BigQuery_TEMP_C"], label="BigQuery TEMP (°C)")
plt.plot(merged_df["fecha"], merged_df["NASA_T2M_C"], label="NASA T2M (°C)")
plt.title("Comparación de Temperaturas - Enero 2022")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Precipitación diaria (NASA)
plt.figure(figsize=(10, 5))
plt.bar(merged_df["fecha"], merged_df["PRECTOTCORR"], color='skyblue')
plt.title("Precipitación Total Diaria (NASA) - Enero 2022")
plt.xlabel("Fecha")
plt.ylabel("Precipitación (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Gráfico combinado: Temperatura (línea) y Precipitación (barras)
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(merged_df["fecha"], merged_df["NASA_T2M_C"], color='tab:red', label="NASA T2M")
ax1.set_ylabel("Temperatura (°C)", color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax2 = ax1.twinx()
ax2.bar(merged_df["fecha"], merged_df["PRECTOTCORR"], alpha=0.3, color='tab:blue', label="Precipitación")
ax2.set_ylabel("Precipitación (mm)", color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:purple')

plt.title("Temperatura y Precipitación - Enero 2022 (NASA)")
fig.tight_layout()
plt.xticks(rotation=45)
plt.show()

# 4. Heatmap de correlación
plt.figure(figsize=(6, 4))
sns.heatmap(merged_df[["BigQuery_TEMP_C", "NASA_T2M_C", "PRECTOTCORR"]].corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación entre Variables")
plt.tight_layout()
plt.show()


merged_df["Diferencia_TEMP"] = merged_df["BigQuery_TEMP_C"] - merged_df["NASA_T2M_C"]

plt.figure(figsize=(10, 5))
plt.plot(merged_df["fecha"], merged_df["Diferencia_TEMP"], marker='o', linestyle='-', color='purple')
plt.title("Diferencia de Temperaturas - BigQuery vs NASA - Enero 2022")
plt.xlabel("Fecha")
plt.ylabel("Diferencia de Temperatura (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

