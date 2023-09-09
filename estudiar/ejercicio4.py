numero_telefono = input("Por favor, introduce un número de teléfono en el formato +34-XXXXXXXXXX-XX: ")

partes = numero_telefono.split("-")

numero_principal = partes[1]

print("El número principal es:", numero_principal)
