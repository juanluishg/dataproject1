import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

berlin_empleo = pd.read_csv('Empleo-Berlin2.csv', delimiter=';', sep=",")


print(berlin_empleo.head())