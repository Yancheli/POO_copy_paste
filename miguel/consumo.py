import pandas as Pd
import json
import requests
from pandas import json_normalize


def consumo():
    variable = "https://WWW.datos.gov.co/resource/fdvb-hsrf.json"
    peticion = requests.get(variable)
    print(peticion)