Lista = [9, 12, 28, 17, 66, 81]
def mergesort(Lista):
    base = len(Lista)
    if base <= 1:
        return Lista
    

    lista_izquierda = Lista[:len(Lista)//2]
    lista_derecha = Lista[len(Lista)//2:]
    lista_izquierda = mergesort(lista_izquierda)
    lista_derecha = mergesort(lista_derecha)



   #print(f'lista original: {Lista} y lista_izquierda: {lista_izquierda}, lista_derecha: {lista_derecha}')
    return None

mergesort(Lista)

def merge(lista_izquierda, lista_derecha):

    lista_resultado = []
    while (len(lista_izquierda)> 0 and len(lista_derecha) > 0):
        if lista_izquierda[0] < lista_derecha[0]:
            lista_resultado.append(lista_izquierda[0])
            lista_izquierda = lista_izquierda[1:]
        else:
            lista_resultado.append(lista_derecha[0])
            lista_derecha = lista_derecha[1:]

    if len(lista_izquierda) > 0:
        lista_resultado += lista_izquierda
    print(lista_resultado)
    return lista_resultado  




mergesort(Lista)          
    