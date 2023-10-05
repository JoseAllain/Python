import pandas as pd
import numpy as np
import datetime as dt
e2016=pd.read_csv('/workspaces/Python/practica 3-e8/emisiones-2016.csv')
e2017=pd.read_csv('/workspaces/Python/practica 3-e8/emisiones-2017.csv')
e2018=pd.read_csv('/workspaces/Python/practica 3-e8/emisiones-2018.csv')
e2019=pd.read_csv('/workspaces/Python/practica 3-e8/emisiones-2019.csv')
df= pd.concat([e2016, e2017, e2018, e2019], ignore_index=True)
fc= df[['ESTACION', 'MAGNITUD','ANO','MES']]
cf= pd.concat([fc, df.loc[:, df.columns[df.columns.str.startswith('D')]]], axis=1)
df_2= cf.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
df_2['DIA'] = df_2.DIA.str.strip('D')
df_2['FECHA'] = df_2.ANO.apply(str) + '/' + df_2.MES.apply(str) + '/' + df_2.DIA.apply(str)
df_2['FECHA'] =pd.to_datetime(df_2.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')
df_2 = df_2.drop(df_2[np.isnat(df_2.FECHA)].index)
df_2.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])
#print('Estaciones:', df_2.ESTACION.unique())
#print('Contaminantes:', df_2.MAGNITUD.unique())
def evolucion (estacion, contaminante, desde, hasta):
    return df_2[(df_2.ESTACION == estacion) & (df_2.MAGNITUD == contaminante) & (df_2.FECHA >= desde) & (df_2.FECHA <= hasta)].sort_values('FECHA').VALOR
#evolucion(56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d'))
df_2.groupby('MAGNITUD').VALOR.describe()
df_2.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()
def resumen(estacion, contaminante):
    return df_2[(df_2.ESTACION == estacion) & (df_2.MAGNITUD == contaminante)].VALOR.describe()

print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', resumen(56, 8),'\n', sep='')
print('Resumen Dióxido de Nitrógeno en Plaza del Carmen:\n', resumen(35, 8), sep='')

