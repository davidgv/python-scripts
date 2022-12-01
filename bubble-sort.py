# Ordenación mediante burbuja (bubble sort)
#   2 variantes:
#     - Ordenación mediante burbuja con recorrido completo
#     - Ordenación mediante burbuja utilizando un flag de corte


def burbuja_completo(lista_original):
# Ordenación mediante burbuja con recorrido completo
  lista_ordenada = lista_original.copy()
  longitud = len(lista_ordenada)
  ciclos = 0 # Contador de ciclos
  cambios = 0 # Número de permutaciones
  for i in range(longitud-1):
    for j in range(longitud-1-i):
      ciclos += 1
      if lista_ordenada[j] > lista_ordenada[j+1] :
        cambios += 1
        lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
  return lista_ordenada, ciclos, cambios


def burbuja_flagdecorte(lista_original):
# Ordenación mediante burbuja utilizando un flag de corte
  lista_ordenada = lista_original.copy()
  longitud = len(lista_ordenada)
  ciclos = 0
  cambios = 0
  for i in range(longitud-1):
    ordenada = True # Flag: está ordenada la lista?
    for j in range(longitud-1-i):
      ciclos += 1
      if lista_ordenada[j] > lista_ordenada[j+1] :
        ordenada = False
        cambios += 1
        lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    if ordenada:
      return lista_ordenada, ciclos, cambios
  return lista_ordenada, ciclos, cambios


# Datos de ejemplo
lista_original = [4, 1, 46, 88, 24, 33, 10, 15, 67, 81, 50]
print(f"Lista original (desordenada): {lista_original}\n")

lista_ordenada, ciclos, cambios = burbuja_completo(lista_original)
print(f"Lista ordenada (mediante burbuja, algoritmo completo): {lista_ordenada}")
print(f"Ciclos: {ciclos}")
print(f"Permutaciones: {cambios}\n")

lista_ordenada, ciclos, cambios = burbuja_flagdecorte(lista_original)
print(f"Lista ordenada (mediante burbuja, con flag de corte): {lista_ordenada}")
print(f"Ciclos: {ciclos}")
print(f"Permutaciones: {cambios}\n")
