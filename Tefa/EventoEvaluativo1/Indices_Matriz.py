# Mostrar los indices de una matriz nxm de forma horizontal

# Mensaje inicial
print("Bienvenido.\nVamos a construir su matriz")

# Toma de datos
n = int(input("Por favor ingrese el número de filas: "))
m = int(input("Por favor ingrese el número de columnas: "))

#Programa o función
def indices(n, m):
    for i in range(n):
        fila = [f"({i},{j})" for j in range(m)]
        print(' '.join(fila))

# Salida
print("Este es el orden de sus índices:")
print(indices(n, m))
