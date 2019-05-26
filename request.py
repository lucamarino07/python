import requests
import pandas
import matplotlib.pyplot as plt

# data_inizio = '2018-02-22'
# data_fine = '2018-05-26'
# base = 'EUR'
# confronto = 'USD'

data_inizio = str(input('Inserisci la data iniziale (yyyy-mm-gg) --> '))
data_fine = str(input('Inserisci la data finale (yyyy-mm-gg) --> '))
base = str(input('Inserisci la valuta di base (esempio EUR) --> '))
confronto = str(input('Inserisci l\' altra valuta --> '))

url = 'https://api.exchangeratesapi.io/history?start_at=' +  data_inizio + '&end_at=' + data_fine + '&base=' + base + '&symbols=' + confronto
response = requests.get(url=url)

data = response.json()

date = list(data['rates'].keys())


valori = [elemento['USD'] for elemento in list(data['rates'].values())]



print('1'*50)


dati = []
colonne = ['Data', 'Valore']
for i in range(len(date)):
     dati.append((date[i],valori[i]))

print('2'*50)

df = pandas.DataFrame.from_records(dati,columns=colonne)
print('3'*50)
output_table = df
print('4'*50)

output_table = (output_table.sort_values(by=['Data'], ascending=True))
print('5'*50)

for i in range(len(date)):
    print(f'Il {output_table.iloc[i, 0]} il rapporto EUR/USD è pari a {output_table.iloc[i, 1]}')

print('6'*50)

chose = input('Vuoi vedere il grafico? [y/n] --> ')

if chose.lower() in ['y', 'yes', 'si', 's']:
    plt.plot(output_table['Data'], output_table['Valore'])
    plt.show()
else:
    print('Addio')

