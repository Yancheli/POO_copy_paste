"""
Este programa es un juego de busqueda del tesoro llamado One Piece

Información a considerar:
    El tablero es una matriz 5x5 lleno de "-".
    Dentro del tablero se encuentra: 1 tesoro (T) y 3 trampas (X).
    El usuario tiene 5 intentos para encontrar el tesoro.
    Si el usuario no logra encontrar el tesoro en 5 intentos, se acaba el juego (pierde)
    Si el usuario selecciona o pisa una trampa (X), pierde inmediatamente
    Si el usuario encuentra el tesoro (T), gana inmediatamente
    Al finalizar el juego se muestra el tablero completo con las ubicaciones de las trampas y el tesoro
"""
# Importamos la libreria random para obtener valores aleatorios
import random

# Se define la dimensión del tablero
filas = 5
columnas = 5

# Se crea el tablero
tablero = [["-" for _ in range(columnas)] for _ in range(filas)]

# Se posiciona el tesoro de manera aleatoria
tesoro_fila = random.randint(0, filas - 1)
tesoro_columna = random.randint(0, columnas - 1)
tablero[tesoro_fila][tesoro_columna] = "T"

# Se posicionan las 3 trampas en posiciones distintas aleatoriamente
trampas_colocadas = 0
while trampas_colocadas < 3:
    f = random.randint(0, filas - 1)
    c = random.randint(0, columnas - 1)
    if tablero[f][c] == "-":
        tablero[f][c] = "X"
        trampas_colocadas += 1

# Tablero oculto para no mostrar las ubicaciones del tesoro y las trampas
tablero_oculto = [["-" for _ in range(columnas)] for _ in range(filas)]

# Se declara valores para el juego
intentos = 5
en_juego = True

# Se crea el bucle y las condicionales para el juego (estructura del juego)
while intentos > 0 and en_juego:
    print("\nTablero actual: ")
    for fila in tablero_oculto:
        print(" ".join(fila))
    
    fila = int(input("Ingrese la fila (0-4): "))
    col = int(input("Ingrese la columna (0-4): "))

    if tablero[fila][col] == "T":
        print("Encontraste el tesoro, ¡Haz ganado!")
        en_juego = False
    elif tablero[fila][col] == "X":
        print("Caiste en una trampa, ¡Haz perdido!")
        en_juego = False
    else:
        print("Aqui no hay nada, Sigue buscando...")
        # Indicador de que la casilla ha sido revisada
        tablero_oculto[fila][col] = "O"
        intentos -= 1
        print(f"Te quedan {intentos} intentos")

# Tablero final con ubicaciones reveladas
print("\nTablero completo: ")
for fila in tablero:
    print(" ".join(fila))