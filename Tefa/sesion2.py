#Contador de vocales: Contar cuantas vocales tiene una cadena ingresada por el usuario, 
# almacenando en un diccionario y pudiendo escoger después que tanto se repitió alguna vocal. 
# El usuario ingresa la información y pregunta el número de veces que se repitió.

# definicion
vocal = "a e i o u"
contar_vocales = {}

#programa
texto = input("Ingrese su texto, por favor")
texto = texto.lower() 


for letra in texto:
    if letra in vocal:
        if letra in contar_vocales:
            contar_vocales[letra] += 1
        else:
            contar_vocales[letra]=1




