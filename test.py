import pandas as pd
import datetime
import random, numpy

numpy.random.seed(12345)

import webbrowser

# webbrowser.open_new('http://www.google.it')


url_google = 'https://maps.google.com/?q='

# df = pd.DataFrame(numpy.random.randint(200, size=(10, 6)))
# print(df)

# df_norm = (df - df.min()) / (df.max() - df.min())
# print(df_norm)

# df_norm = (df - df.mean()) / (df.std())
# print(df_norm)


url = 'https://opendata.comune.palermo.it/ws.php?id=1702&fmt=csv'
df1 = pd.read_csv(url, sep=';', header = 0)

for i in range(5):
    nord = df1['Y'].head(5)[i].replace(',','.')
    est =  df1['X'].head(5)[i].replace(',','.')
    url_google_total = url_google + nord + ',' + est
    webbrowser.open_new(url_google_total)





# df1['Inc2'] = df1.Incidenti.apply(convert_incidente)

# print(df1.head(5))