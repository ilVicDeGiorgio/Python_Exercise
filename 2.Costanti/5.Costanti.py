# Definire una costante per il numero di giorni in una settimana e usarla per calcolare 
# quante settimane ci sono in 365 giorni.

GIORNI_SETTIMANA = 7

GIORNI_ANNO = 365

def calcoloSettimaneAnno():
    settimaneAnno = GIORNI_ANNO / GIORNI_SETTIMANA
    return settimaneAnno

print(calcoloSettimaneAnno())