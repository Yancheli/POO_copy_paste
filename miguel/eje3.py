def factorial(numero):
        if numero == 0:
         return 1 
        else:
         return  numero * factorial(numero - 1)
        
#print("El factorial de 5 es:", factorial(5))

def fibonacci(numero):
   if numero <= 1:
       return numero
   else: 
      return fibonacci(numero - 1) + fibonacci(numero - 2) 
#print(fibonacci(4))

def sumarlista(lista):
   if not lista:
       return 0
   else:
      return lista[0] + sumarlista(lista[1:])
listica = [1,5,2,8]
   #print("La suma de la lista es:", sumarlista(listica))
#print(f"suma lista es : {sumarlista(listica)}")

def invertir(letras):
   if letras == "":
         return ""
   else:
       primer = letras[0]
       sobrante = letras[1:]
       return invertir(sobrante) + primer

print(f"vamos a invertir la cadena *hola* y queda {invertir('hola')}")  