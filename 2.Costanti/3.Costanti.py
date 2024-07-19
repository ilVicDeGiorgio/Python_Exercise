# Definire una costante per il tasso di cambio euro-dollaro e usarla per convertire 100 euro in dollari.

TASSO_EUR_USD = 1.1

def cambioMoneta(euro):
    dollari = euro * TASSO_EUR_USD
    return dollari

print(cambioMoneta(15))

