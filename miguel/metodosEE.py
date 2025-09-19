import requests
import pandas as pd
import json
from pandas import json_normalize
 
link = 'https://www.datos.gov.co/api/v3/views/gjy9-tpph/query.json'
APP_TOKEN = "gvuPkSYHkxGir5hjFtAMJF4ii"
 
headers = {"X-App-Token": APP_TOKEN}
 
peticion = requests.get(link, headers=headers)
print(peticion)
 
if peticion.status_code == 200:
    combustible = peticion.json()
    print(combustible)
else:
    print("Error en la petición:", peticion.text)


    lista = [10, 4, 23,2,50, 19]
def quick(Lista):
    base = len(Lista)
    if base <= 1:
        return Lista
    

    pivote = Lista.pop()
    lista_izquierda = []
    lista_derecha = []


    for i in Lista: 
        if i <= pivote: 
            lista_izquierda.append(i)
        else:
            lista_derecha.append(i)

    print(f'lista original: {Lista} y pivote: {pivote}, lista_izquierda: {lista_izquierda}, lista_derecha: {lista_derecha}') 

    lista_izquierda = quick(lista_izquierda)
    lista_derecha = quick(lista_derecha)
    
    
    
    
    return lista_izquierda + [pivote] + lista_derecha



print(quick(lista))   






def obtener_datos_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

# 3. Flujo principal del programa
if __name__ == "__main__":
    url_api = "https://www.datos.gov.co/api/v3/views/gjy9-tpph/query.json"
    
    datos_api = obtener_datos_api(url_api)
    
    if datos_api:
        # Extraer los IDs de las publicaciones y guardarlos en una nueva lista
        ids = [post['id'] for post in datos_api]
        
        print("IDs de la API sin ordenar:", ids)
        
        # Llamar a la función Quick Sort con la lista de IDs
        ids_ordenados = quick(ids)
        
        print("\nIDs de la API ordenados:", ids_ordenados)