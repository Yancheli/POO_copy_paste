# Este programa muestra los indices de una matriz NxM de forma horizontal cambiando de direccion

# Solicitamos las dimensiones para la matriz
n = int(input("Ingrese el número de filas para la matriz (n): "))
m = int(input("Ingrese el número de columnas para la matriz (m): "))

# Se crea y añade valores a la matriz
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        valor = input(f"Ingrese el valor para la posición ({i},{j}): ")
        fila.append(valor)
    matriz.append(fila)

# Mostramos la matriz ingresada en forma horizontal y cambiando la dirección en cada salto de fila (zigzag)
print("\nMatriz en orden zigzag: ")
for i in range(n):
    # Fila par (0,2,4...) va de izquierda a derecha
    if i % 2 == 0:
        for j in range(m):
            print(matriz[i][j], end = " ")
    # Fila impar (1,3,5...) va de derecha a izquierda
    else:
        for j in range(m - 1, -1, -1):
            print(matriz[i][j], end = " ")
    # Salto de linea para cambiar a la siguiente fila
    print()
