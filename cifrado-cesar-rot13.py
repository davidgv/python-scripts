# Algoritmo de Cifrado César (ROT13)

def cifrado_ROT13(cadena):
  cadena_cifrada = ""
  for i in range(len(cadena)):
    letra = cadena[i]
    ascii = ord(cadena[i])
    if (ascii >= 65 and ascii <= 77) or (ascii >= 97 and ascii <= 109): # A-M > N-Z
      cadena_cifrada += chr(ascii+13)
    elif (ascii >= 78 and ascii <= 90) or (ascii >= 110 and ascii <= 122): # N-Z > A-M
      cadena_cifrada += chr(ascii-13)
    else: # resto inmutable
      cadena_cifrada += letra
  return cadena_cifrada

print("ALGORITMO DE CIFRADO CÉSAR (ROT13)")

texto = input("Texto a cifrar ? ")
texto_cifrado = cifrado_ROT13(texto)
texto_descifrado = cifrado_ROT13(texto_cifrado)

print(f"Cadena original: {texto}")
print(f"Cadena cifrada: {texto_cifrado}")
print(f"Cadena descifrada: {texto_descifrado}") # para descifrar, aplicamos de nuevo el algoritmo
