import numpy as np
import glob
import pandas as pd

ruta_directorio = '/workspaces/Python/Practica 4-f/'

patron = '*.xls'

archivos_xls = glob.glob(ruta_directorio + patron)

dataframes = []

for archivo in archivos_xls:
    df = pd.read_excel(archivo, skiprows=4)
    nombre=archivo.split('/')[-1]
    df['nombre'] = nombre
    dataframes.append(df)

dataset = pd.concat(dataframes, ignore_index=True)

#print(dataset)

#Ejer 2

num_filas = dataset.shape[0]
num_columnas = dataset.shape[1]
#print(f'Filas: {num_filas}, Columnas: {num_columnas}')

#Ejer 3

#print(dataset.head(10))

#Ejer 4

dataset=dataset.rename(columns={'Estación': 'estacion','Provincia':'provincia','Temperatura máxima (ºC)':'temp_max','Temperatura mínima (ºC)':'temp_min','Temperatura media (ºC)':'temp_med','Racha (km/h)':'viento_racha','Velocidad máxima (km/h)':'viento_vel_max','Precipitación 00-24h (mm)':'prec_dia','Precipitación 00-06h (mm)':'prec_0_6h','Precipitación 06-12h (mm)':'prec_6_12h','Precipitación 12-18h (mm)':'prec_12_18h','Precipitación 18-24h (mm)':'prec_18_24h','nombre':'fecha'})
dataset.head(1)
print (dataset)

#Ejer 5
dataset=dataset.replace(to_replace=r'.\(.+\)$', value='', regex=True)
dataset.head(1)
#print (dataset)

#Ejer 6
dataset.fecha=dataset.fecha.replace(regex={'Aemet':'',r'\.+xls':''})
dataset.head(1)
#print (dataset)

#Ejer 7
#dataset.info()

#Ejer 8
dataset=dataset.astype({'estacion': 'string','provincia': 'string', 'temp_max':'float64', 'temp_min':'float64', 'viento_racha':'float64', 'viento_vel_max':'float64','fecha': 'datetime64[ns]'})
dataset['fecha']=pd.to_datetime(dataset["fecha"].dt.strftime('%Y-%m-%d'))
#dataset.info()

#Ejer 9
nulos=dataset[dataset.isnull().any(axis=1)]['estacion'].unique()
dataset.drop(dataset[dataset['estacion'].isin(nulos)].index, inplace=True)
#print(dataset.isna().sum())


#Ejer 10
#print(dataset.iloc[:,np.r_[0:8,12:13]].describe())

#Ejer 19

dataset_diff = dataset.select_dtypes(include=['float64']).diff()

# Agregar las diferencias como una nueva fila
dataset_diff = dataset_diff.rename(index={idx: f'{col}_diff' for idx, col in enumerate(dataset_diff.index)})

# Concatenar el DataFrame original con las diferencias como una nueva fila
dataset = pd.concat([dataset, dataset_diff])

# Mostrar el resultado
print(dataset)

