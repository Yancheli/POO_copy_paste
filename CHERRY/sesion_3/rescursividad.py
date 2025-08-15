"""
def facto(numero):
    if numero == 0:
        return 1
    else:
        return numero * facto(numero - 1)
    
#print(facto(5))
"""
"""
def fibo(numero):
    if numero <= 1:
        return numero
    else:
        return fibo(numero - 1) + fibo(numero - 2)

print(fibo(7))
"""
"""
def sumaLista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumaLista(lista[1:])

listica = [1,5,2,8]
print(f"suma lista es: {sumaLista(listica)}")
"""
"""
def invertir(letras):
    if letras == "":
        return ""
    else:
        primer = letras[0]
        sobrante = letras[1:]
        return invertir(sobrante) + primer

print(f"Vamos a invertir la cadena hola y queda {invertir("hola")}")
"""