import pandas as pd
import os

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

os.chdir('C:/Users/JuanLu/Dropbox/I.Informatica/Master/dataproject1/Data/Berlin')


temp = pd.read_csv("normalize/temp_prep_luz.csv")

temp_media = temp.groupby('Year')['temp_media'].mean()

print(temp_media)

