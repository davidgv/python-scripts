# Dibujando un árbol de Navidad en la terminal

altura = 0
while altura < 5:
  altura = int(input("¿Altura del árbol de Navidad? (min.5) : "))
ancho = (altura*2)-1

def insert_espacios(cuantos):
  cadena_espacios = ""
  for i in range(cuantos):
    cadena_espacios += " "
  return cadena_espacios

for i in range(altura):
  linea = ""

  if i == altura-1: # base del árbol => dibujar tronco
    num_espacios = ancho - 3
    linea += insert_espacios(num_espacios//2)
    linea += "|||"
    linea += insert_espacios(num_espacios//2)

  else: # no es tronco => dibujar hojas
    num_hojas = (i*2)+1
    num_espacios = ancho - num_hojas
    linea += insert_espacios(num_espacios//2)
    for j in range(num_hojas):
      linea += "*"
    linea += insert_espacios(num_espacios//2)

  print(linea)
