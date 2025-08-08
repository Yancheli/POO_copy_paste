# Contador de vocales enuna cadena

# Ingreso de la cadena por el ususario
texto = input("Ingrese una cadena de texto: ").lower()

# Diccionario contable de vocales
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Conteo de vocales
for letra in texto:
    if letra in vocales:
        vocales[letra] += 1

# Consultar el conteo de una vocal en bucle
while True:
    consulta = input("\n¿Qué vocal desea consultar? (a, e, i, o, u o 'salir'): ").lower()
    
    if consulta == "salir":
        print("Saliendo del programa...")
        break
    elif consulta in vocales:
        print(f"La vocal '{consulta}' se repitió {vocales[consulta]} veces")
    else:
        print("Error al ingresar la vocal")