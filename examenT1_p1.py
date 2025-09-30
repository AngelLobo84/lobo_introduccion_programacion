# varieble que recibe el monto en soles
soles = input("Ingresa el monto en soles: ")
# variable que recibe la tasa de cambio dolares
dolar = input("ingresa tasa de cambio actual:")


# Operación de cálculo de soles a dolares:
cambio_dolar = float(soles) / float(dolar)
print ()
print (f"monto ingresado en soles es: {soles}")
print (f"tipo de cambio ingresado es: {dolar}")
print (f"el cambio de soles a dolares es: {cambio_dolar:.2f}")