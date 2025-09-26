
#metodo burbuja
lista = [6, 10, 24, 67, 2, 15]
def burbuja(lista):
    tamaño  = len(lista)
    for i in range(tamaño):
        #print(lista)
        for j in range(0, tamaño-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



burbuja(lista)    

#seleccion
#lista = [8, 1, 75, 48, 14, 20]
def seleccion(lista):
    tamaño = len(lista)
    for i in range(tamaño):
        min_indice = i
        print(lista)

        for j in range(i + 1, tamaño):
            if lista[j] < lista[min_indice]:
                min_indice = j
    
        lista[i], lista[min_indice] = lista[min_indice], lista[i]        

    return lista
#seleccion(lista)





