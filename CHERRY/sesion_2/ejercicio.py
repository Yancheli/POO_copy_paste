# Variable nombre
nombre = input("Introduce tu nombre")
# Variable edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad < 18:
    print(f"Eres menor de edad {nombre}")
else:
    print(f"Eres mayor de edad {nombre}")