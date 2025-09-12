lista = [3, 16, 7, 56, 97, 31]
def insercion(lista):
    tamaño = len(lista)
    for i in range(1, tamaño):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j - 1

        lista[j + 1] = valor
        print(lista)
    
    
    return lista


insercion(lista)