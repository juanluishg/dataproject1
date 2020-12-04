# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:29:57 2020

@author: ampbo
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import scipy.stats as stats  # For statistical inference 
import seaborn as sns  # For hi level, Pandas oriented, graphics

# Get working directory
os.getcwd()

# Change working directory
os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//CLIMA')

os.getcwd()

#Reads data from CSV file and stores it in a dataframe called rentals_2011
# Pay atention to the specific format of your CSV data (; , or , .)
CLIMA=pd.read_csv("clima_de_1955a2020.csv", sep=';', decimal=',', encoding='gbk')
print(CLIMA.shape)
print(CLIMA.head())
print(CLIMA.info()) 
CLIMA.describe()
print(CLIMA)

#SEGREGAR AÑO DE REF_DATE
a=str(CLIMA.REF_DATE)
a[:4]
#for a in CLIMA.REF_DATE

year=[]
month=[]
for a in CLIMA.REF_DATE:
    aux=str(a)
    year.append(aux[:4])
    month.append(aux[4:6])

#una vez segregados año y día en unos objetos diferentes, hay que append a la tabla. 
dates=pd.DataFrame({'year':year,'month': month})
clima2= pd.concat([CLIMA, dates], axis=1)

#GRUPOS POR TEMPERATURAS
clima2.groupby('year').T.mean()

#nueva tabla sólo con la información a partir del año 2000:
clima3 = clima2.loc[(clima2['year']>='2000')]

#GRUPOS POR TEMPERATURAS
clima3.groupby('year').T.mean()
clima3.groupby('month').T.mean()

#CONFECCIONAR UNA TABLA ÚNICAMENTE CON LA TEMPERATURA POR AÑO. MEDIA
CLIMA_temp=CLIMA[my_vars]
CLIMA_temp.shape
my_vars=['T', 'REF_DATE']


#Días de lluvia al mes y año
clima3.groupby('year').NUM_PRECP_01.mean()
clima3.groupby('month').NUM_PRECP_01.mean()


#guardar variable clima 3

clima3.to_csv('clima3.csv')


#población del último año. Disponemos de una tabla con la población por distritos 
os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//POBLACION_CENSO')

poblacion=pd.read_csv("evolucion_poblacion_1869a2020_vie_101.csv", sep=';', decimal=',')

year=[]
month=[]
for a in poblacion.REF_DATE:
    aux=str(a)
    year.append(aux[:4])
    month.append(aux[4:6])

#una vez segregados año y día en unos objetos diferentes, hay que append a la tabla. 
dates=pd.DataFrame({'year':year,'month': month})
poblacion= pd.concat([poblacion, dates], axis=1)

#nueva tabla sólo con la información a partir del año 2019:
poblacion_act = poblacion.loc[(poblacion['year']>='2019')]

poblacion_act.groupby('DISTRICT_CODE').POP_TOTAL.sum() #este no aporta una mierder
poblacion_act.groupby('year').POP_TOTAL.sum()


#guardar la variable población
poblacion_act.to_csv('poblacion_act.csv')


#QC OK

# PIB

os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//ECONOMÍA//PIB')

PIB=pd.read_csv("API_GC.TAX.TOTL.GD.ZS_DS2_en_csv_v2_1745131.csv", sep=',', decimal='.', encoding='UTF-8')

print(PIB.shape)
print(PIB.head())
print(PIB.info()) 
PIB.describe()
print(PIB)

PIB2 = PIB.loc[(PIB['Country Name']=='Austria')]

print(PIB2.shape)
print(PIB2.head())
print(PIB2.info()) 
PIB2.describe()
print(PIB2)

PIB3=np.transpose(PIB2, axes=None) '''lo transpone, pero el problema es que en el encabezado se aplican 4 filas que
no es el nombre de la columna''' 

PIB3.to_csv('PIB.csv')


PIB=pd.read_csv("PIB.csv", sep=',', decimal='.', encoding='UTF-8')

PIB4 = PIB.loc[(PIB['Year']=='2018')]
PIB4.to_csv('PIB2018.csv')


#QC OK

#IPC 

os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//ECONOMÍA//IPC')
IPC=pd.read_csv("API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_1740201.csv", sep=',', decimal='.', encoding='UTF-8')

print(IPC.shape)
print(IPC.head())
print(IPC.info()) 
IPC.describe()
print(IPC)


IPC2 = IPC.loc[(PIB['Country Name']=='Austria')]

print(IPC2.shape)
print(IPC2.head())
print(IPC2.info()) 
IPC2.describe()
print(IPC2)

IPC3=np.transpose(IPC2, axes=None)    
IPC3.to_csv('IPC.csv')

IPC=pd.read_csv("PIB.csv", sep=',', decimal='.', encoding='UTF-8')
IPC=IPC.rename(columns={IPC.columns[1]:'Indicador'})
IPC4 = IPC.loc[(PIB['Year']>='2000')]

import math as math

IPC4 =IPC4.reset_index()[['Year','Indicador']]
n2 = IPC4.Indicador[0]
aux = []
aux.append(0)
for i in range(1, len(IPC4.Indicador)):
    n1 = IPC4.Indicador[i]
    if n1 == n2:
        aux.append(0)
    else:
        res = (math.log(n1)-math.log(n2))/(n1-n2)
        aux.append(res)
        n2 = IPC4.Indicador[i]

variacion = pd.DataFrame({'Variacion': aux})

res = pd.concat([IPC4, variacion], axis=1)

res.to_csv('IPC_res.csv')

#revenue tax

os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//ECONOMÍA//TAX REVENUE')
tax=pd.read_csv("tax_revenue.csv", sep=',', decimal='.', encoding='UTF-8')


print(tax.shape)
print(tax.head())
print(tax.info()) 
tax.describe()
print(tax)


tax2 = tax.loc[(tax['Country Name']=='Austria')]

print(tax2.shape)
print(tax2.head())
print(tax2.info()) 
tax2.describe()
print(tax2)

tax3=np.transpose(tax2, axes=None)    
tax3.to_csv('tax.csv')

tax4=pd.read_csv("tax.csv", sep=',', decimal='.', encoding='UTF-8')

tax = tax4.loc[(tax4['Year']>='2010')]

tax.to_csv('tax.csv')


PIB4=PIB3.dropna("nan")
print(PIB3.shape)


#cálculo ratio museos por habitante


os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//csv_convertidos')
museos=pd.read_csv("museos.csv", sep=';')

a=101/1911191*100000

os.chdir('C://Users//ampbo//OneDrive//Escritorio//EDEM//PROYECTO QUALITYLIFE//dataproject1//Data//Viena//csv_convertidos')
life_exp1=pd.read_csv('Life_expentancy_vienne.csv', sep=';', decimal='.')




# web scraping. MUSEOS VIENA

import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd 

# Ruta para indicar la ubicación del driver necesario para la biblioteca webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Le decimos al driver de chrome de que url sacar la información
driver.get('https://www.olx.com.ec/autos_c378')



# Buscamos el boton de cargar más 
# Vamos a darle al boton 3 veces

boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        time.sleep(random.uniform(5.0, 10.0))
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

# Marcamos donde estan todos los anuncios de una lista
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

precio = list()
descripcion = list ()               #creamos las listas para almacenar los datos

for auto in autos:                  #creamos un for para meter cada dato en su lista
    precio.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text)
   
    
    descripcion.append(auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text)
    
   
   
    
   
#con la libreria pandas creamos la tabla. 
    
dict = {'Coches': descripcion,'Precio':precio}

df = pd.DataFrame(dict)

print(df)

from bs4 import BeautifulSoup
import requests
import pandas as pd 

url = 'https://www.wien.info/es/sightseeing/museums-exhibitions/top'      #le decimos la url a la que le sacaremos la información
page = requests.get(url)                                                        # Nos descargamos el contenido de la página 
soup = BeautifulSoup(page.content, 'html.parser')                               # Aqui con el comando BeautifulSoup hacemos más manejables los datos

eq = soup.find_all('h3', class_="tile_headline h2")

museos = list()

count = 0

for i in eq:
  if count < 8:
    museos.append(i.text)
  else:
    break
  count += 1
print(museos, len(museos))