correo = input("Por favor, introduce tu correo electrónico: ")
nombre_usuario, dominio = correo.split('@')
nuevo_correo = f"{nombre_usuario}@ceu.es"

print("Nuevo correo electrónico:", nuevo_correo)
