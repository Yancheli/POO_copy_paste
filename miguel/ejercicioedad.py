Nombre = input("ingresa tu nombre: ")
print("Hola, " + Nombre + "!")  
Edad = input("Ingresa tu edad: ")
Edad = int(Edad)
if Edad < 18:
    print(f"Eres menor de edad. {Nombre}")
else:
    print(f"Eres mayor de edad. {Nombre}")