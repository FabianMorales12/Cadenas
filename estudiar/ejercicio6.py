frase = input("Por favor, introduce una frase: ")

vocal = input("Introduce una vocal: ")

vocal = vocal.lower()
frase_con_vocal_mayuscula = frase.replace(vocal, vocal.upper())

print("Frase con la vocal en mayúscula:", frase_con_vocal_mayuscula)
