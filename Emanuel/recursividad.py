def facto(numero):
    if numero == 0:
        return 1
    else:
        numero * facto(numero - 1)
print(facto(0))

def fibo(numero):
    if numero <= 1:
        return numero
    else:
        return fibo(numero - 1) + fibo(numero - 2)
    
print(fibo(7))

def sumalista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sumalista(lista[1:])
    
listica = [1,5,2,8]
print(f"suma lista es: {sumalista(listica)}")