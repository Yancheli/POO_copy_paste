import requests
def insertion_sort(nums, asc=True):
    a = nums[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        if asc:
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key
    return a

def merge(left, right, asc=True):
    res = []
    i = j = 0
    if asc:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def merge_sort(nums, asc=True):
    n = len(nums)
    if n <= 1:
        return nums[:]
    mid = n // 2
    left = merge_sort(nums[:mid], asc=asc)
    right = merge_sort(nums[mid:], asc=asc)
    return merge(left, right, asc=asc)

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

print("Insertion Sort:", insertion_sort(precios, asc=asc)[:20])
print("Merge Sort:", merge_sort(precios, asc=asc)[:20])