import requests
import pandas as pd
from pandas import json_normalize
 
# ------------------- CONSUMO DE API -------------------
link = 'https://www.datos.gov.co/api/v3/views/gjy9-tpph/query.json'
APP_TOKEN = "gvuPkSYHkxGir5hjFtAMJF4ii"
 
headers = {"X-App-Token": APP_TOKEN}
 
try:
    r = requests.get(link, headers=headers, timeout=20)
    r.raise_for_status()
    payload = r.json()
except Exception as e:
    print("Error en la petición:", e)
    payload = None
 
# ------------------- EXTRACCIÓN DE PARÁMETR -------------------
precios = []
if payload:
    # Normalización
    df = pd.json_normalize(payload)
 
    #Revisión de fila
    print("Ejemplo de fila:", payload[0])
 
    # recorrido
    for row in payload:
        try:
            if "precio" in row:
                precios.append(float(row["precio"]))
 
            elif isinstance(row, list):
                precios.append(float(row[8]))
        except Exception:
            pass
 
print("Lista de precios extraída:", precios[12])
 
# ------------------- ALGORITMOS -------------------
class RadixSort:
    def ordenar(self, arr, ascendente=True):
        if not arr:
            return arr
 
        arr = [int(x) for x in arr]
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self._counting_sort(arr, exp, ascendente)
            exp *= 10
        return arr
 
    def _counting_sort(self, arr, exp, ascendente):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
 
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
 
        if ascendente:
            for i in range(1, 10):
                count[i] += count[i - 1]
        else:
            for i in range(8, -1, -1):
                count[i] += count[i + 1]
 
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
 
        for i in range(n):
            arr[i] = output[i]
 
 
class BucketSort:
    def ordenar(self, arr, ascendente=True):
        if not arr:
            return arr
 
        arr = [float(x) for x in arr]
        n = len(arr)
        max_val, min_val = max(arr), min(arr)
 
        bucket_count = n
        buckets = [[] for _ in range(bucket_count)]
 
        for num in arr:
            index = int((num - min_val) / (max_val - min_val + 1) * (bucket_count - 1))
            buckets[index].append(num)
 
        for i in range(bucket_count):
            buckets[i] = sorted(buckets[i], reverse=not ascendente)
 
        resultado = []
        for bucket in buckets:
            resultado.extend(bucket)
 
        return resultado
 
 
# ------------------- PROGRAMA PRINCIPAL -------------------
if __name__ == "__main__":
    if not precios:
        print("No se pudieron extraer precios de la API.")
        exit()
 
    print("Algoritmos disponibles:")
    print("1. RadixSort")
    print("2. BucketSort")
 
    opcion = input("Seleccionar algoritmo: ")
    orden = input("¿Quieres orden ascendente? (s/n): ")
 
    ascendente = True if orden.lower() == "s" else False
 
    if opcion == "1":
        sorter = RadixSort()
    elif opcion == "2":
        sorter = BucketSort()
    else:
        print("Opción inválida")
        exit()
 
    resultado = sorter.ordenar(precios, ascendente=ascendente)
 
    print("\nDatos originales (primeros 10):", precios[:10])
    print("Datos ordenados (primeros 10):", resultado[:10])