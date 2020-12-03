import pandas as pd
import os
import numpy as np
import math

from datetime import datetime, timedelta


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

os.chdir('./Data/Berlin/')

def temperature():
    temp = pd.read_csv("temp_1963-2018.txt", sep=";")
    temp2 = pd.read_csv("temp_2019.txt", sep=";")

    #print(temp.tail())
    #print(temp2.head())
    data=pd.DataFrame(columns=temp.columns)
    for j in range(1, 6):
        date = '2017'+"{:02d}".format(j)+'01'
        newDate = '2019'+"{:02d}".format(j)+'01'
        #print(date)
        res = temp[temp['MESS_DATUM_BEGINN'] == int(date)]
        a = pd.DataFrame(res)
        #print(a.dtypes)
        a['MESS_DATUM_BEGINN'] = a['MESS_DATUM_BEGINN']+20000
        a['MESS_DATUM_ENDE'] = a['MESS_DATUM_ENDE']+20000
        data = data.append(a , ignore_index=True)

    #print(data)
    final_temp = pd.concat([temp, data, temp2], ignore_index=True)
    print(temp2.head())

    final_temp = final_temp[['STATIONS_ID','MESS_DATUM_BEGINN', 'MESS_DATUM_ENDE', 'MO_TT', 'MO_RR', 'MO_SD_S']]
    final_temp = final_temp.rename(columns={'STATIONS_ID':'id_estacion','MESS_DATUM_BEGINN':'fecha_inicio', 'MESS_DATUM_ENDE':'fecha_fin', 'MO_TT':'temp_media', 'MO_RR':'sum_precipitacion', 'MO_SD_S':'horas_luz'})
    final_temp.to_csv("normalize/temp_prep_luz.csv")

def num_precipitaciones_al_mes():
    prep = pd.read_csv("precipitaciones_por_dia.txt", sep=";")
    num_prep_dias = pd.DataFrame(columns={'id_estacion', 'fecha', 'num_dias'})
    prep.columns = prep.columns.str.replace(' ', '')

    year = []
    month = []
    days = []
    for a in prep.MESS_DATUM:
        aux = str(a)
        year.append(aux[:4])
        month.append(aux[4:6])
        days.append(aux[6:])

    dates = pd.DataFrame({'Year': year, 'Month': month, 'Day': days})

    prep = pd.concat([prep, dates], axis=1)

    sum_df = prep.groupby(['Year','Month', 'Day']).agg({'RS':'sum'})

    sum_df.loc[(sum_df['RS'] > 0), 'Lluvia'] = 1
    sum_df.loc[(sum_df['RS'] == 0), 'Lluvia'] = 0

    sum_df = sum_df.groupby(['Year','Month']).agg({'Lluvia':'sum'})

    sum_df.to_csv('normalize/num_dias_lluvia.csv')


def poblacion():
    columns = ['Region','Year','Population','Persons in employment','Unemployed persons','Economically active population','Economically inactive population']
    pob = pd.read_csv("Población-Paro-Alemania-Por-Regiones.csv", sep=";", encoding='ansi',header=None, names=columns, skiprows=7)

    berlin = pob[pob['Region'].str.contains('Berlin')]
    res = berlin[['Region', 'Year', 'Population']]
    res[['Population']] = res[['Population']]*1000

    columns = ['Region', 'Size(sq km)']
    size = pd.read_csv("Tamaño-Territorio-Por-Regiones.csv", sep=";", encoding='ansi',header=None, names=columns, skiprows=6)

    berlin_sz = size[size['Region'].str.contains('Berlin')]

    res = pd.merge(res, berlin_sz, on="Region")

    res['pob/km2'] = res['Population']/res['Size(sq km)']

    res.to_csv("normalize/poblacion_superficie.csv")

def arte():

    art = pd.read_csv("Indicadores_culturales_Por_Regiones.csv", sep=";", encoding="ansi", header=0, skiprows=4)
    art = art.rename(columns={art.columns[0]:'Region', art.columns[1]:'Type'})

    berlin = art[art['Region'].str.contains('Berlin')]

    pob = pd.read_csv('normalize/poblacion_superficie.csv')
    pob_year = pob[pob['Year'].str.startswith('20')]

    years = list(berlin.columns[2:].values)

    newDf = pd.DataFrame({'Region': 'Berlin', 'Year':years, 'Museums': 0, 'Theaters': 0, 'Cinemas':0},columns=['Region', 'Year', 'Museums', 'Theaters', 'Cinemas'])
    #print(newDf.head())

    mus = berlin[berlin['Type'] == 'Museums per 100,000 inhabitants']
    mus = mus.drop(['Region', 'Type'], axis=1)
    mus = mus.transpose()
    mus = (mus.values.tolist())
    flattened = [val for sublist in mus for val in sublist]
    pop = pob['Population'].values.tolist()
    
    res = []
    for i in range(0, len(pop)):
        res.append(mus[i] * (pop[i]/100000))

    print(res)

"""
year = []
month = []
for a in CLIMA.REF_DATE:
    aux = str(a)
    year.append(aux[:4])
    month.append(aux[4:6])

dates = pd.Dataframe({'Year': year, 'Month': month})

CLIMA = pd.concat([CLIMA, dates], axis=1)
"""


def ipc ():
    ipc = pd.read_csv('IPC-por-CA.csv', sep=";", encoding="ansi", header=0, skiprows=4)
    ipc = ipc.rename(columns={ipc.columns[0]:'Year'})

    ipc = ipc.dropna(axis=0, how='any')
    #print(ipc.tail())

    #(ln(n)-ln(n-1))/n-(n-1)
    #n1 = n
    #n2 = n-1

    n2 = ipc.Berlin[0]
    aux = []
    aux.append(0)
    for i in range(1, len(ipc.Berlin)):
        n1 = ipc.Berlin[i]
        if n1 == n2:
            aux.append(0)
        else:
            res = (math.log(n1)-math.log(n2))/(n1-n2)
            aux.append(res)
            n2 = ipc.Berlin[i]

    variacion = pd.DataFrame({'Variacion': aux})

    res = pd.concat([ipc, variacion], axis=1)

    res = res[['Year', 'Berlin', 'Variacion']]

    res.to_csv("normalize/ipc_con_variacion.csv")


def pib():
    pib = pd.read_csv('PIB_Por_Regiones.csv', sep=";", encoding="ansi", header=0, skiprows=6)
    pib = pib.rename(columns={pib.columns[0]:'Year'})
    pib = pib.dropna(axis=0, how='any')

    ppp = pd.read_csv("DP_LIVE_03122020201426740.csv", sep=",")

    berlin_pib = pib[['Year', 'Berlin']]

    berlin_pib['Year'] = berlin_pib['Year'].astype(int)

    berlin_pib = berlin_pib.loc[(berlin_pib['Year']>=2000)]

    berlin_pib = berlin_pib.reset_index()

    ppp = ppp.loc[(ppp['LOCATION'] == 'DEU')]

    ppp = ppp[['TIME', 'Value']]

    ppp = ppp.rename(columns={'TIME':'Year'})

    newDf = pd.merge(berlin_pib, ppp, on='Year')

    newDf['ppp'] = newDf['Berlin'] * newDf['Value']

    newDf = newDf[['Year','Berlin','Value','ppp']]

    newDf.to_csv("normalize/pib_in_ppp.csv")