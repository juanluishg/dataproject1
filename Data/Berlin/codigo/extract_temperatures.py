import pandas as pd
import requests
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


anyos = np.arange(2010, 2021, step=1)
meses = np.arange(1, 13, step=1)

for i in anyos:
    for j in meses:
        #Del 2010 al 2017 estan en historical
        if i < 2018:
            #Los meses van con dos cifras
            if j < 10:
                filename = 'gradtage_'+ str(i) + '0' + str(j) +'.csv'
                url = 'https://opendata.dwd.de/climate_environment/CDC/derived_germany/techn/monthly/heating_degreedays/hdd_3807/historical/'+filename
                r = requests.get(url, allow_redirects=True)
                open('./Data/Berlin/temperature/' + filename, 'wb').write(r.content)
            else:
                filename = 'gradtage_'+ str(i) + str(j) +'.csv'
                url = 'https://opendata.dwd.de/climate_environment/CDC/derived_germany/techn/monthly/heating_degreedays/hdd_3807/historical/'+filename
                r = requests.get(url, allow_redirects=True)
                open('./Data/Berlin/temperature/' + filename, 'wb').write(r.content)
        else:
            url = 'https://opendata.dwd.de/climate_environment/CDC/derived_germany/techn/monthly/heating_degreedays/hdd_3807/recent/'
            #Los meses van con dos cifras
            if j < 10:
                filename = 'gradtage_'+ str(i) + '0' + str(j) +'.csv'
                r = requests.get(url+filename, allow_redirects=True)
                open('./Data/Berlin/temperature/' + filename, 'wb').write(r.content)
            else:
                filename = 'gradtage_'+ str(i) + str(j) +'.csv'
                r = requests.get(url+filename, allow_redirects=True)
                open('./Data/Berlin/temperature/' + filename, 'wb').write(r.content)