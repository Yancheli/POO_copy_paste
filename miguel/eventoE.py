import random

def mostrar_indices_horizontal():
    try:
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
        return

    if filas <= 0 or columnas <= 0:
        print("Las dimensiones deben ser números enteros positivos.")
        return

    print("Índices de la matriz en forma horizontal:")
    for i in range(filas):
        for j in range(columnas):
            print(f"({i},{j})", end=" ")
        print() 

mostrar_indices_horizontal()

 

TAMAÑO_TABLERO = 5
NUM_TRAMPAS = 3
INTENTOS = 5



def crear_tablero():
 
    return [['-' for _ in range(TAMAÑO_TABLERO)] for _ in range(TAMAÑO_TABLERO)]

def colocar_elementos(tablero):

    posiciones_ocupadas = []

    while True:
        fila = random.randint(0, TAMAÑO_TABLERO - 1)
        columna = random.randint(0, TAMAÑO_TABLERO - 1)
        if (fila, columna) not in posiciones_ocupadas:
            tablero[fila][columna] = 'T'
            posiciones_ocupadas.append((fila, columna))
            break

    for _ in range(NUM_TRAMPAS):
        while True:
            fila = random.randint(0, TAMAÑO_TABLERO - 1)
            columna = random.randint(0, TAMAÑO_TABLERO - 1)
            if (fila, columna) not in posiciones_ocupadas:
                tablero[fila][columna] = 'X'
                posiciones_ocupadas.append((fila, columna))
                break

    def colocar_elementos(tablero):
                posiciones_ocupadas = []

                # colocar tesoro
                while True:
                    fila = random.randint(0, TAMAÑO_TABLERO - 1)
                    columna = random.randint(0, TAMAÑO_TABLERO - 1)
                    if (fila, columna) not in posiciones_ocupadas:
                        tablero[fila][columna] = 'T'
                        tesoro = (fila, columna)
                        posiciones_ocupadas.append(tesoro)
                        break

                # colocar trampas iniciales
                trap_positions = []
                for _ in range(NUM_TRAMPAS):
                    while True:
                        fila = random.randint(0, TAMAÑO_TABLERO - 1)
                        columna = random.randint(0, TAMAÑO_TABLERO - 1)
                        if (fila, columna) not in posiciones_ocupadas:
                            tablero[fila][columna] = 'X'
                            posiciones_ocupadas.append((fila, columna))
                            trap_positions.append((fila, columna))
                            break

                return tesoro, trap_positions


def mover_trampas(tablero, trap_positions, tesoro):
                # limpiar trampas viejas
                for (r, c) in trap_positions:
                    if tablero[r][c] == 'X':
                        tablero[r][c] = '-'

                nuevas = []
                while len(nuevas) < len(trap_positions):
                    r = random.randint(0, TAMAÑO_TABLERO - 1)
                    c = random.randint(0, TAMAÑO_TABLERO - 1)
                    if (r, c) == tesoro:
                        continue
                    if tablero[r][c] == '-' and (r, c) not in nuevas:
                        tablero[r][c] = 'X'
                        nuevas.append((r, c))

                return nuevas



def mostrar_tablero_final(tablero):
    
    print("\n asi queda el tablero final:")
    for fila in tablero:
        print(" ".join(fila))
    print("---------------------")



def jugar_busqueda_tesoro():
    
    tablero = crear_tablero()
    colocar_elementos(tablero)
    
    intentos_restantes = INTENTOS
    juego_terminado = False

    print("¡Bienvenido a la Búsqueda del Tesoro!")
    print(f"Tienes {INTENTOS} intentos para encontrar el tesoro (T). ¡Cuidado con las trampas (X)!")

    while intentos_restantes > 0 and not juego_terminado:
        print(f"\nIntentos restantes: {intentos_restantes}")
        
        try:
            mostrar_tablero_final(tablero)
            fila_usr = int(input("Ingresa la fila (0-4): "))
            col_usr = int(input("Ingresa la columna (0-4): "))

            if not (0 <= fila_usr < TAMAÑO_TABLERO and 0 <= col_usr < TAMAÑO_TABLERO):
                print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
                continue

        except ValueError:
            print("Entrada inválida. Por favor, ingresa números.")
            continue

    
        casilla = tablero[fila_usr][col_usr]

        if casilla == 'T':
            print("\n¡Felicidades! ¡Has encontrado el tesoro!")
            juego_terminado = True
        elif casilla == 'X':
            print("\n¡Oh no! ¡Caíste en una trampa! Has perdido.")
            juego_terminado = True
        else: 
            print("No hay nada en esa casilla.")
            intentos_restantes -= 1

    if not juego_terminado:
        print("\n¡Te has quedado sin intentos! El juego ha terminado.")

    mostrar_tablero_final(tablero)

jugar_busqueda_tesoro()


#correciones con gemini 2.5