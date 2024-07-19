# Definire una costante per il valore della gravità terrestre e usarla per calcolare il peso di 
# un oggetto di massa 10 kg.

massa = 10

GRAVITA_TERRESTRE = 9.81

def calcolaPeso():
    pesoOggetto = massa * GRAVITA_TERRESTRE
    return pesoOggetto

print(calcolaPeso())