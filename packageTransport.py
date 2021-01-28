peso = 41.5
transporte = 300

# Envío terrestre
if peso <= 2:
    precio = peso * 1.5 + transporte
elif (peso > 2) and (peso <= 6):
    precio = peso * 3 + transporte
elif (peso > 6) and (peso <= 10):
    precio = peso * 4 + transporte
else:
    precio = peso * 4.75 + transporte

print("El envío terrestre cuesta $", precio)


# Envío maritimo
envioMaritimo = 500
print("El envío maritimo cuesta $", envioMaritimo)

# Envío aereo
if peso <= 2:
    precio = peso * 4.5
elif (peso > 2) and (peso <= 6):
    precio = peso * 9
elif (peso > 6) and (peso <= 10):
    precio = peso * 12
else:
    precio = peso * 14.25

print("El envío aereo cuesta $", precio)