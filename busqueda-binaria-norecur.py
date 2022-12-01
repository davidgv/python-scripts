# Búsqueda binaria sin recursividad

def busbin(lis, ini, fin, num):
  while ini <= fin:
    med = ini+(fin-ini)//2
    if lis[med] > num:
      fin = med-1
    elif lis[med] < num:
      ini = med+1
    else:
      return med
  return -1

# Datos de prueba
lista = [-100, -91, -15, 2, 23, 24, 56, 61, 87, 99, 100] # debe estar ordenada
buscado = -15

ibuscado = busbin(lista, 0, len(lista)-1, buscado)

if ibuscado == -1:
  print("El número no está en la lista")
else:
  print(f"El número ocupa el índice {ibuscado} en la lista")
