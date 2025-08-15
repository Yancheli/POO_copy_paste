#Primero tomo la librería
import random

# Creación del tablero de juego
tablero = [["-" for _ in range(5)] for _ in range(5)]

# Pongo tesoro y trampas aleatoriamente
def colocar (tablero, marca):
    while True:
        fila = random.randint(0, 4)
        colu = random.randint(0, 4)
        if tablero[fila][colu] == "-":
            tablero[fila][colu] = marca
            break

colocar(tablero, "T")

# Colocar 3 trampas(base)
for _ in range(3):
    colocar(tablero, "X")

# Entorno del jugador
Entorno_visible = [["-" for _ in range(5)] for _ in range(5)]

# Juego
intentos = 5
juego = True

while intentos > 0 and juego:
    print("\nTablero:")
    for fila in Entorno_visible:
        print(" ".join(fila))

    try:
        fila = int(input("Ingresa fila(0-4): "))
        colu = int(input("Ingresa columna(0-4): "))
    except ValueError:
        print("Revisa tu número...")
        continue

    if fila < 0 or fila > 4 or colu < 0 or colu > 4:
        print("Revisa tus coordenadas...Fuera de rango")
        continue

    if tablero[fila][colu] == "T":
        print("¡Aquí está el tesoro! Bien hecho")
        juego = False
    elif tablero[fila][colu] == "X":
        print("Tocaste un bloque que ya había convertido en bomba...mala suerte")
        juego = False
    else:
        print("No era ahí...")
        Entorno_visible[fila][colu] = "-"
        intentos -= 1
        print(f"Intentos restantes: {intentos}")

if intentos == 0 and juego:
    print("¡Que mal! Se te acabaron los intentos")

# Finalización
print("\nPosiciones finales:")
for fila in tablero:
    print(" ".join(fila))
