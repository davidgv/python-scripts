# Generación de una matriz m x n de enteros aleatorios en el intervalo [a,b]

import random

# Esta es la matriz que queremos calcular
matriz = []

# Variables
m = 10    # filas de la matriz
n = 10    # columnas de la matriz
a = -1000 # límite inferior aleatorio (incluido)
b = 1000  # límite superior aleatorio (incluido)

# Algoritmo de relleno de la matriz
for fila in range(m):
  lista_fila = []
  for colu in range(n):
    alea = random.randint(a,b)
    lista_fila.append(alea)
  matriz.append(lista_fila)

print(matriz)
