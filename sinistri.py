import csv

def print_menu(dizionario):
    print(' '*50)
    print(' '*50)
    print(f'{"*"*20}MENU{"*"*20}')
    print(' '*50)
    print(' '*50)
    for key in dizionario.keys():
        print(f'Inserisci {key} se vuoi filtrare per {dizionario[key]}')
    print(f'Inserisci ESC per uscire')
    print(' '*50)

incidenti_dict = {
    'C': 'Incidente con danni materiali ai mezzi',
    'F': 'Incidente con feriti',
    'R': 'Incidente con prognosi riservata',
    'M': 'Incidente mortale'
}

incidenti_dict2 = {
    'C': 'con danni materiali ai mezzi',
    'F': 'con feriti',
    'R': 'con prognosi riservata',
    'M': 'con morti'
}

inc_sing_plur = {
    1: 'incidente',
    2: 'incidenti'
}

print_menu(incidenti_dict)

while True:
    scelta = ''
    while scelta not in (incidenti_dict.keys()) and scelta.upper() != 'ESC':
        scelta = str(input('--> ')).upper()
        
        if scelta in (incidenti_dict.keys()) or scelta.upper() == 'ESC':
            break
        else:
            print('Scelta errata, riprova!')

    if scelta.upper() == 'ESC':
        print('Fine')
        break
    else:
        print(' '*50)
        with open("./sinistri.csv", newline="") as filecsv:
            lettore = csv.reader(filecsv, delimiter=";")
            dati = [(linea) for linea in lettore if linea[3] == scelta]

            if len(dati) == 1:
                sing_plur = 1
            else:
                sing_plur = 2

            for incidente in dati:
                print(f"{incidenti_dict[incidente[3]]} avvenuto il {incidente[0]} alle \
        ore {incidente[1]} in {incidente[2]}")

        print(' '*50)
        print('-'*50)
        print(' '*50)
        print(f'Ci sono stati {len(dati)} {inc_sing_plur[sing_plur]} {incidenti_dict2[scelta]} nel 2018')
        print_menu(incidenti_dict)