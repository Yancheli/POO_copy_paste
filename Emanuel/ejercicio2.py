asignaturas = {
    "POO": 'B12', 
    "Matematicas Discretas" : 'B11', 
    "Calculo": 'B10',
    "Fundamentos": 'B09',}

usuario = input("ingresa la asignatura que quieres consultar: ")
print(asignaturas[usuario])
 
cadena = input("Ingresa una cadena de texto: ")
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in cadena.lower():
    if letra in vocales:
        vocales[letra] += 1

print("Conteo de vocales:", vocales)

vocal_a_consultar = input("¿Qué vocal quieres consultar? ")
if vocal_a_consultar.lower() in vocales:
    print(f"La vocal '{vocal_a_consultar}' aparece {vocales[vocal_a_consultar.lower()]} veces.")
else:
    print("Eso no es una vocal.")

#Copilot ayudo