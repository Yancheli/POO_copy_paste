# Ejercicio Evaluativo 1
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matriz de izquierda a derecha y de izquierda a derecha
for i in range(len(matriz)):
    fila = matriz[i]
    if i % 2 == 0:

        for num in fila:
            print(num, end=" ")
    else:
        for num in reversed(fila):
            print(num, end=" ")

    print()






#Programa Busca del tesoro
import random

# se crea el tablero
def crear_tablero(tamaño):
    return [["-" for _ in range(tamaño)] for _ in range(tamaño)]

# Colocar tesoro y trampas
def colocar_elementos(tablero):
    tamaño = len(tablero)
    posiciones = set()

    # Colocar tesoro
    while True:
        fila_w, col_w = random.randint(0, tamaño-1), random.randint(0, tamaño-1)
        if (fila_w, col_w) not in posiciones:
            tablero[fila_w][col_w] = "W"
            posiciones.add((fila_w, col_w))
            break

    # Colocar trampas
    trampas = 3
    while trampas > 0:
        fila_x, col_x = random.randint(0, tamaño-1), random.randint(0, tamaño-1)
        if (fila_x, col_x) not in posiciones:
            tablero[fila_x][col_x] = "X"
            posiciones.add((fila_x, col_x))
            trampas -= 1

# Mostrar tablero oculto
def mostrar_tablero(tablero, revelar=False):
    for fila in tablero:
        if revelar:
            print(" ".join(fila))
        else:
            print(" ".join(["-" if celula in ["W", "X"] else celula for celula in fila]))

# Juego
def jugar():
    tamaño = 5
    intentos = 5
    tablero = crear_tablero(tamaño)
    colocar_elementos(tablero)

    print("Hola, esto es Busca el tesoro")
    while intentos > 0:
        mostrar_tablero(tablero)
        try:
            fila = int(input("Ingresa la fila (0-4): "))
            col = int(input("Ingresa la columna (0-4): "))
        except ValueError:
            print("Numero invalido, Usa números del 0 al 4.")
            continue

        if not (0 <= fila < tamaño and 0 <= col < tamaño):
            print("Numero no existe")
            continue

        celda = tablero[fila][col]
        if celda == "W":
            print("Encontraste el tesoro, Ganaste")
            break
        elif celda == "x":
            print("Has caido en una trampa, Fin del juego.")
            break
        else:
            print("Fallaste, no esta aqui, sigue buscando.")
            intentos -= 1
            tablero[fila][col] = "F"  # Marca la celda como visitada

    if intentos == 0:
        print("has perdido todos los intentos. Fin del juego.")

    print("\nTablero final:")
    mostrar_tablero(tablero, revelar=True)

jugar()

#Ayuda de copilot