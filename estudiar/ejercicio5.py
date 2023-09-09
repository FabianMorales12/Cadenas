frase = input("Por favor, introduce una frase: ")
palabras = frase.split()

palabras.reverse()

frase_invertida = ' '.join(palabras)

print("Frase invertida:", frase_invertida)
