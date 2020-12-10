# -*- coding: utf-8 -*-
"""Análisis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IgGsebdiJRAdXOeW7I9wXXZQAtyPXlXQ

Install dependencies
"""
#%reset -f

#!pip install psycopg2

"""Import libraries"""

import psycopg2
import numpy as np
import pandas as pd
import time


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

"""[Connect to database](https://pynative.com/python-postgresql-tutorial/)"""

def algoritmo():
    
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "Welcome01",
                                      host = "34.78.89.69",
                                      port = "5432",
                                      database = "dataproject1")
    
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
    
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    
    """Obtain "datos" of the cities and columns names"""
    
    cursor.execute("SELECT * FROM datos;")
    record = cursor.fetchall()
    
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'datos'")
    columns_name = cursor.fetchall()
    
    """Convert array of arrays to single array"""
    
    array_columns_name = np.array(columns_name)
    array_columns_name = np.concatenate( array_columns_name, axis=0 )
    
    #print(array_columns_name)
    
    """Transform result of query to a pandas dataframe"""
    
    df = pd.DataFrame(record, columns=array_columns_name)
    
    df.head()
    
    """Obtain "clientes" of the clients responses"""
    
    cursor.execute("SELECT * FROM clientes ORDER BY client_id DESC;")
    record = cursor.fetchall()
    
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'clientes'")
    columns_name = cursor.fetchall()
    
    array_columns_name = np.array(columns_name)
    array_columns_name = np.concatenate( array_columns_name, axis=0 )
    
    clientes = pd.DataFrame(record, columns=array_columns_name)
    
    clientes.head()
    
    df['score'] = 0
    
    
    """Pollution Variable"""
    
    env_score = clientes.iloc[0].enviromental_score
    pollution_cities = pd.DataFrame(columns=df.columns)
    #print(env_score)
    if env_score == 5:
      min = df.pollution.min()
      df.loc[df.pollution == min, 'score'] +=1
      pollution_cities = df[df.pollution == min]
    elif env_score == 4:
      order_by_pollution = df.sort_values(by=['pollution'], ascending=True)
      mins = order_by_pollution.iloc[:2]
      for _, i in mins.iterrows():
        df.loc[df.city_id == i.city_id, 'score'] += 1
        pollution_cities = pollution_cities.append(i)
    elif env_score == 3:
      order_by_pollution = df.sort_values(by=['pollution'], ascending=True)
      mins = order_by_pollution.iloc[:3]
      for _, i in mins.iterrows():
        df.loc[df.city_id == i.city_id, 'score'] += 1
        pollution_cities = pollution_cities.append(i)
    elif env_score == 2:
      order_by_pollution = df.sort_values(by=['pollution'], ascending=True)
      mins = order_by_pollution.iloc[:4]
      for _, i in mins.iterrows():
        df.loc[df.city_id == i.city_id, 'score'] += 1
        pollution_cities = pollution_cities.append(i)
    elif env_score == 1:
      order_by_pollution = df.sort_values(by=['pollution'], ascending=True)
      mins = order_by_pollution.iloc[:5]
      for _, i in mins.iterrows():
        df.loc[df.city_id == i.city_id, 'score'] += 1
        pollution_cities = pollution_cities.append(i)
    
    #df.head()
    
    """Work Spaces Variable"""
    
    wk_space = clientes.iloc[0].work_preference
    wk_cities = pd.DataFrame(columns=df.columns)
    if wk_space == 'Co-Working':
      ratio = df['work_spaces'] /df['c_population']
      aux = df
      aux['ratio'] = ratio*100
      aux.loc[aux.ratio > 0.006, 'score'] +=1
      wk_cities = aux.loc[aux.ratio>0.006]
      #print(aux.head())
    
    #wk_cities
    
    """Transport Variable"""
    
    a = {'Walking': 'Andando', 'Car': 'Coche', 'Bike': 'Bici', 'Motorbike': 'Moto', 'Bus/Trolleybus': 'Bus', 'Tram/Streetcar': 'Tranvía', 'Train/Metro': 'Metro'}
    df.best_mobility_option.replace(a, inplace=True)
    
    clientex = clientes.iloc[0].transport
    df.loc[df.best_mobility_option == clientex, 'score']+=1
    transport_cities = df.loc[df.best_mobility_option == clientex]
    
    
    """
    cliente = clientes.iloc[0].transport
    for _, i in df.iterrows():
      if i.best_mobility_option == cliente:
        df.score[df.city_id == i.city_id] += 1
    print(df.head())
    """
    
    cliente= clientes.iloc[0]
    
    #df.loc[(df.mountain == True & cliente.place_score == 'Montaña' & df.beach  == False, 'score'] =+ 1
    
    """Landscape Variable"""
    
    landscape_cities = pd.DataFrame(columns=df.columns)
    for _, i in df.iterrows():
      if i.mountain == True and i.beach == False and cliente.place_score == 'Montaña':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        landscape_cities = landscape_cities.append(i)
      elif i.mountain == False and i.beach == True and cliente.place_score == 'Playa':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        landscape_cities = landscape_cities.append(i)
      elif i.mountain == True and i.beach == True and cliente.place_score == 'Ambos':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        landscape_cities = landscape_cities.append(i)
      elif i.mountain == False and i.beach == False and cliente.place_score == 'Ninguno':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        landscape_cities = landscape_cities.append(i)
    
    
    
    """Weather Variable"""
    
    weather_cities = pd.DataFrame(columns= df.columns)
    for _, i in df.iterrows():
      if (i.c_temp < 15 or i.c_rainy_days > 20) and cliente.season == 'Invierno':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        weather_cities = weather_cities.append(i)
      elif (15 <= i.c_temp <= 25 or  10 <= i.c_rainy_days) <= 20 and cliente.season == 'Primavera':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        weather_cities = weather_cities.append(i)
      elif (i.c_temp > 25 or i.c_rainy_days < 10) and cliente.season == 'Verano':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        weather_cities = weather_cities.append(i)
      elif (15 <= i.c_temp <= 25 or  10 <= i.c_rainy_days <= 20) and cliente.season == 'Otoño':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        weather_cities = weather_cities.append(i)
    
    """Housing Variable"""
    
    housing_cities = pd.DataFrame(columns=df.columns)
    for _, i in df.iterrows():
      if i.housing and cliente.percentaje_home > 50:
        df.loc[df.city_id == i.city_id, 'score'] += 1
        housing_cities = housing_cities.append(i)
      elif i.housing < 15 and 30 <= cliente.percentaje_home <= 50:
        df.loc[df.city_id == i.city_id, 'score'] += 1
        housing_cities = housing_cities.append(i)
      elif i.housing < 5 and cliente.percentaje_home < 30:
        df.loc[df.city_id == i.city_id, 'score'] += 1
        housing_cities = housing_cities.append(i)
    
    """Size Variable"""
    
    size_cities = pd.DataFrame(columns=df.columns)
    for _, i in df.iterrows():
      if i.c_population < 2000000 and cliente.size_preference == 'Pequeñas':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        size_cities = size_cities.append(i)
      elif 2000000 <= i.c_population <= 4000000 and cliente.size_preference == 'Medianas':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        size_cities = size_cities.append(i)
      elif i.c_population > 4000000 and cliente.size_preference == 'Grandes':
        df.loc[df.city_id == i.city_id, 'score'] += 1
        size_cities = size_cities.append(i)
    
    """Leisure Variable"""
    
    leisure_cities = pd.DataFrame(columns=df.columns)
    if cliente.entreteiment == 'Sí':
      max_leisure = df.leisure.max()
      df.loc[df.leisure == max_leisure, 'score'] += 1
      leisure_cities = df[df.leisure == max_leisure]
    
    """Non-client Variables"""
    
    min_cpi = df.cpi.min()
    df.loc[df.cpi == min_cpi, 'score'] += 0.5
    
    max_gdp= df.gdp_pc.max()
    df.loc[df.gdp_pc == max_gdp, 'score'] += 0.5
    
    min_tax = df.tax_burden.min()
    df.loc[df.tax_burden == min_tax, 'score'] += 0.5
    
    min_crime = df.crime_rate.min()
    df.loc[df.crime_rate == min_crime, 'score'] += 0.5
    
    max_hdi = df.hdi.max()
    df.loc[df.hdi == max_hdi, 'score'] += 0.5
    
    max_doing_business = df.doing_business.max()
    df.loc[df.doing_business == max_doing_business, 'score'] += 0.5
    
    max_freedom = df.freedom.max()
    df.loc[df.freedom == max_freedom, 'score'] += 0.5
    
    max_life = df.life_expectancy.max()
    df.loc[df.life_expectancy == max_life, 'score'] += 0.5
    

    """Factor"""
    factor = clientes.iloc[0].interest_variable
    if factor == 'Medio ambiente':
      for _, i in pollution_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Zona de trabajo':
      for _, i in wk_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Tamaño de la ciudad':
      for _, i in size_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Ocio':
      for _, i in leisure_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Gasto en vivienda':
      for _, i in housing_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Clima':
      for _, i in weather_cities.iterrows():
        df.loc[i == df.city_id, 'score']+=1
    elif factor == 'Movilidad urbana':
      for _, i in transport_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
    elif factor == 'Paisaje':
      for _, i in landscape_cities.iterrows():
        df.loc[i.city_id == df.city_id, 'score']+=1
        
            
    """ELEGIR CIUDAD"""
    
    ciudad_ideal = df[df.score == df.score.max()]
    #print(ciudad_ideal)
    print("Tu ciudad ideal es: "+ ciudad_ideal.city_name + "\n")
    print("con una puntuación de: "+str(ciudad_ideal.score))
    
    
    cursor = connection.cursor()
    cursor.execute(
      "UPDATE clientes SET best_city_name1='"+ciudad_ideal.iloc[0].city_name+"'"+
      " WHERE client_id = "+str(clientes.iloc[0].client_id));
    connection.commit()
    cursor.close()
    
    if len(ciudad_ideal) >= 2:
        cursor = connection.cursor()
        cursor.execute(
          "UPDATE clientes SET best_city_name1='"+ciudad_ideal.iloc[1].city_name+"'"+
          " WHERE client_id = "+str(clientes.iloc[0].client_id));
        connection.commit()
        cursor.close()
    
    return ciudad_ideal

def main():
    while True:
        ciudad = algoritmo()
        time.sleep(5)

if __name__ == "__main__":
    main()

