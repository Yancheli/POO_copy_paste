import requests
import pandas as pd
import heapq

def burbuja(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascendente and lista[j] > lista[j + 1]) or (not ascendente and lista[j] < lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def seleccion(lista, ascendente=True):
    n = len(lista)
    for i in range(n):
        idx_extremo = i
        for j in range(i + 1, n):
            if (ascendente and lista[j] < lista[idx_extremo]) or (not ascendente and lista[j] > lista[idx_extremo]):
                idx_extremo = j
        lista[i], lista[idx_extremo] = lista[idx_extremo], lista[i]
    return lista

def insertion_sort(nums, asc=True):
    a = nums[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        if asc:
            while j >= 0 and a[j] > key:
                a[j+1] = a[j]; j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j+1] = a[j]; j -= 1
        a[j+1] = key
    return a

def merge(left, right, asc=True):
    res = []
    i = j = 0
    if asc:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: res.append(left[i]); i += 1
            else: res.append(right[j]); j += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]: res.append(left[i]); i += 1
            else: res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def merge_sort(nums, asc=True):
    n = len(nums)
    if n <= 1:
        return nums[:]
    m = n // 2
    return merge(merge_sort(nums[:m], asc), merge_sort(nums[m:], asc), asc)

def quick3(nums, asc=True):
    if len(nums) <= 1:
        return nums[:]
    p = nums[len(nums)//2]
    menores = [x for x in nums if x < p]
    iguales = [x for x in nums if x == p]
    mayores = [x for x in nums if x > p]
    res = quick3(menores, asc) + iguales + quick3(mayores, asc)
    return res if asc else res[::-1]

def counting_sort(nums, asc=True):
    if not nums:
        return []
    ints = [int(round(x*100)) for x in nums]
    mn, mx = min(ints), max(ints)
    cnt = [0]*(mx-mn+1)
    for v in ints: cnt[v-mn] += 1
    out = []
    for i,c in enumerate(cnt):
        if c: out.extend([i+mn]*c)
    res = [x/100 for x in out]
    return res if asc else res[::-1]

def radix_sort(nums, asc=True):
    if not nums:
        return []
    arr = [int(round(x*100)) for x in nums]
    mn = min(arr)
    if mn < 0:
        shift = -mn
        arr = [x+shift for x in arr]
    else:
        shift = 0
    mx = max(arr)
    exp = 1
    while mx//exp > 0:
        out = [0]*len(arr)
        cnt = [0]*10
        for v in arr: cnt[(v//exp)%10] += 1
        for i in range(1,10): cnt[i] += cnt[i-1]
        for i in range(len(arr)-1,-1,-1):
            d = (arr[i]//exp)%10
            out[cnt[d]-1] = arr[i]
            cnt[d] -= 1
        arr = out
        exp *= 10
    if shift:
        arr = [x-shift for x in arr]
    res = [x/100 for x in arr]
    return res if asc else res[::-1]

def bucket_sort(nums, asc=True):
    if not nums:
        return []
    a = nums[:]
    n = len(a)
    mn, mx = min(a), max(a)
    if mx == mn:
        return a
    bcount = max(10, min(100, n//50 if n>=50 else n))
    buckets = [[] for _ in range(bcount)]
    for x in a:
        idx = int((x-mn)/(mx-mn+1e-12)*(bcount-1))
        buckets[idx].append(x)
    res = []
    for b in buckets:
        b.sort(reverse=not asc)
        res.extend(b)
    return res

def heap_sort(nums, asc=True):
    if asc:
        h = nums[:]
        heapq.heapify(h)
        return [heapq.heappop(h) for _ in range(len(h))]
    else:
        h = [-x for x in nums]
        heapq.heapify(h)
        return [-heapq.heappop(h) for _ in range(len(h))]

link = "https://www.datos.gov.co/api/views/gjy9-tpph/rows.json"
APP_TOKEN = "gvuPkSYHkxGir5hjFtAMJF4ii"
headers = {"X-App-Token": APP_TOKEN}

peticion = requests.get(link, headers=headers, timeout=20)
print("Código de respuesta:", peticion.status_code)

if peticion.status_code == 200:
    combustible = peticion.json()
    cols = [c["name"] for c in combustible["meta"]["view"]["columns"]]
    df = pd.DataFrame(combustible["data"], columns=cols)

    print("\nColumnas disponibles:")
    for i, col in enumerate(df.columns):
        print(f"{i}. {col}")

    col_index = int(input("\nElige el número de la columna que quieras ordenar: ").strip())
    columna = df.iloc[:, col_index]

    try:
        columna_numerica = pd.to_numeric(columna, errors="coerce").dropna().astype(float).tolist()
    except Exception as e:
        print("La columna no es numérica:", e)
        raise SystemExit(1)

    if not columna_numerica:
        print("No hay datos numéricos en la columna seleccionada.")
        raise SystemExit(1)

    print("\nDatos originales (primeros 10):", columna_numerica[:10])

    print("\nElige un algoritmo de ordenamiento:")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Merge")
    print("5. Quick")
    print("6. Counting")
    print("7. Radix")
    print("8. Bucket")
    print("9. Heap")
    opcion = input(">> ").strip()

    print("\nElige el orden:")
    print("1. Ascendente")
    print("2. Descendente")
    orden = input(">> ").strip()
    ascendente = True if orden == "1" else False

    metodos = {
        "1": burbuja,
        "2": seleccion,
        "3": insertion_sort,
        "4": merge_sort,
        "5": quick3,
        "6": counting_sort,
        "7": radix_sort,
        "8": bucket_sort,
        "9": heap_sort,
    }

    if opcion in metodos:
        resultado = metodos[opcion](columna_numerica.copy(), ascendente)
        print("\nResultado ordenado (primeros 10):", resultado[:10])
    else:
        print("Opción no válida")
else:
    print("Error en la petición:", peticion.status_code)

#equipo copy_paste: Emanuel Pulgarin, Miguel Arboleda, Yancelly Estefania,Samuel Garcia, Emanuel Cano