import pandas as pd
import os
import numpy as np
import math

from datetime import datetime, timedelta


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

os.chdir('C:/Users/JuanLu/Dropbox/I.Informatica/Master/dataproject1/Data/Berlin')

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

    year = []
    month = []
    days = []
    for a in final_temp.MESS_DATUM_BEGINN:
        aux = str(a)
        year.append(aux[:4])
        month.append(aux[4:6])
        days.append(aux[6:])

    dates = pd.DataFrame({'Year': year, 'Month': month})

    final_temp = pd.concat([final_temp, dates], axis=1)

    final_temp = final_temp[['STATIONS_ID','Year', 'Month', 'MO_TT', 'MO_RR', 'MO_SD_S']]
    final_temp = final_temp.rename(columns={'STATIONS_ID':'id_estacion', 'MO_TT':'temp_media', 'MO_RR':'sum_precipitacion', 'MO_SD_S':'horas_luz'})
    final_temp.to_csv("normalize/temp_prep_luz.csv", index=False)

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

    sum_df= sum_df.groupby(['Year','Month']).agg({'Lluvia':'sum'})

    sum_df = sum_df.reset_index(level=['Year', 'Month'])

    sum_df =sum_df.rename(columns={'Lluvia':'num_dias_lluvia'})
    
    sum_df.to_csv('normalize/num_dias_lluvia.csv', index=False)

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

    res.to_csv("normalize/poblacion_superficie.csv", index=False)

def arte():

    art = pd.read_csv("Indicadores_culturales_Por_Regiones.csv", sep=";", encoding="ansi", header=0, skiprows=4)
    art = art.rename(columns={art.columns[0]:'Region', art.columns[1]:'Type'})

    berlin = art[art['Region'].str.contains('Berlin')]

    res = berlin.loc[(berlin.Type == 'Museums per 100,000 inhabitants')]
    a = berlin.loc[berlin.Type == 'Cinemas (screens) per 100,000 inhabitants']

    res = pd.concat([res, a], axis=0)
    
    res.to_csv("normalize/museums_cinemas_per_100000.csv", index=False)

arte()

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

    res.to_csv("normalize/ipc_con_variacion.csv", index=False)


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

    newDf.to_csv("normalize/pib_in_ppp.csv", index=False)

def esperanza():
    vida = pd.read_csv("Esperanza_de_Vida_Por_Regiones.csv", sep=";", header=0, skiprows=5, encoding='ansi')
    vida = vida.rename(columns={vida.columns[0]:'Gender', vida.columns[1]:'Region'})

    vida = vida.loc[(vida.Region == 'Berlin')]
    print(vida.head())

    vida.to_csv("normalize/esperanza_vida.csv", index=False)

def revenue_taxes():
    tax = pd.read_csv("Revenue_Tax.csv", sep=",", header=0, skiprows=3)

    berlin_tax = tax.loc[(tax['Country Name'] == 'Germany')]

    berlin_tax = berlin_tax.dropna(axis=1)
    
    print(berlin_tax.head())

    berlin_tax.to_csv("normalize/revenue_taxes.csv", index=False)

#temperature()
#num_precipitaciones_al_mes()
#poblacion()
#arte()
#ipc()
#pib()
#esperanza()
#revenue_taxes()