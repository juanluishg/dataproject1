import pandas as pd
import os
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

os.chdir('./Data/Berlin/temperature')

anyos = np.arange(2010, 2021, step=1)
meses = np.arange(1, 13, step=1)

header = ['station_id', 'geogr Breite', 'geogr Laenge', 'Station',  'Monat',  'Anzahl Tage', 'Monatsgradtage',  'Anzahl Heiztage', 'Mittelwert']


aux = pd.DataFrame()


for i in anyos:
    for j in meses:
        filename =  'gradtage_'
        if j < 10:
            filename+= str(i)+ '0' + str(j) + '.csv'
        else:
            filename+= str(i)+ str(j) + '.csv'

        try:
            temp = pd.read_csv(filename, sep=';', comment="#", header=None, names=header)
            print(filename)
            a = temp[temp['Station'].str.contains("BERLIN")]
            res = a[['Station', 'Monat', 'Anzahl Tage','Monatsgradtage']]
            aux = aux.append(res, ignore_index=True)
            #print(res.head())
        except:
            print("error")

aux = aux.rename(columns={'Station': 'estacion', 'Monat': 'año/mes', 'Anzahl Tage': 'Dias por mes','Monatsgradtage':'Grados'})
#print(aux.head())

res = aux.groupby('año/mes').mean()['Grados']/aux.groupby('año/mes').mean()['Dias por mes']
res = res.rename(index={0: 'año/mes', 1: 'grados'})

res.to_csv("salida.csv")

