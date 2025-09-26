
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