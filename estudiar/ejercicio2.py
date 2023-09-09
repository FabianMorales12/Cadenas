
nombre_completo = input("Por favor, introduce tu nombre completo: ")
nombre_min = nombre_completo.lower()
print("Nombre completo en minúsculas:", nombre_min)
nombre_may = nombre_completo.upper()
print("Nombre completo en mayúsculas:", nombre_may)
palabras = nombre_completo.split()
nombre_cap = ' '.join([palabra.capitalize() for palabra in palabras])
print("Nombre con la primera letra en mayúscula:", nombre_cap)
