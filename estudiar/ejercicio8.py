precio_str = input("Por favor, introduce el precio en euros (con dos decimales): ")
precio_decimal = float(precio_str)
euros = int(precio_decimal)
centimos = int((precio_decimal - euros) * 100)
print("Euros:", euros)
print("Céntimos:", centimos)
