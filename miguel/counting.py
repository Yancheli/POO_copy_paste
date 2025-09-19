lista= [2,7,4,1,3,6]
def counting(Lista):
    auxiliar = [0 for i in range (10)]
    resultado = [0 for i in range (len(Lista))]


    for i in Lista:
        auxiliar[i] += 1
    
    for i in range(1, 10):
        auxiliar[i] += auxiliar[i-1]
    #print(auxiliar)


    for i in range(len(Lista)):
        resultado[auxiliar[Lista[i]] - 1] = Lista[i]
        auxiliar[Lista[i]] -= 1



    return resultado
print(counting(lista))        



import pandas as pd
import _json
from pandas import json_normalize


def consumo():
    variable = "https://WWW.datos.gov.co/resource/fdvb-hsrf.json"
    peticion = requests.get(variable)
    print(peticion)
