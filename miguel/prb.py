import requests

def quick3(nums, asc=True):
    if len(nums) <= 1:
        return nums[:]
    pivote = nums[len(nums) // 2]
    menores = [x for x in nums if x < pivote]
    iguales = [x for x in nums if x == pivote]
    mayores = [x for x in nums if x > pivote]
    resultado = quick3(menores, asc) + iguales + quick3(mayores, asc)
    return resultado if asc else resultado[::-1]

def counting_sort(nums, asc=True):
    if not nums:
        return []
    nums_int = [int(round(x * 100)) for x in nums]
    max_val = max(nums_int)
    min_val = min(nums_int)
    rango = max_val - min_val + 1
    conteo = [0] * rango
    for num in nums_int:
        conteo[num - min_val] += 1
    resultado = []
    for i, c in enumerate(conteo):
        resultado.extend([i + min_val] * c)
    resultado = [x / 100 for x in resultado]
    return resultado if asc else resultado[::-1]

link = "https://www.datos.gov.co/resource/gjy9-tpph.json?$limit=5000"
APP_TOKEN = "gvuPkSYHkxGir5hjFtAMJF4ii"
headers = {"X-App-Token": APP_TOKEN}

r = requests.get(link, headers=headers, timeout=20)
r.raise_for_status()
payload = r.json()

precios = []
for row in payload:
    try:
        precios.append(float(row["precio"]))
    except Exception:
        pass

modo = input("¿Quieres el orden asc o desc? ").strip().lower()
asc = True if modo == "asc" else False

print("Quick Sort:", quick3(precios, asc=asc)[:20])
print("Counting Sort:", counting_sort(precios, asc=asc)[:20])
