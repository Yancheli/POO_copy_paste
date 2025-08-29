import requests
import pandas as pd
import json
from pandas import json_normalize

link = 'https://pokeapi.co/api/v2/pokemon/ditto'
peticion = requests.get(link)
print(peticion)
pokemones = json.loads(peticion.text)
print(pokemones)