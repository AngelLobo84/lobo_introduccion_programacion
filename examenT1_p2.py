# varieble que recibe el la edad del pasajero
edad = input("Ingresa la edad del pasajero: ")

# Operación de cálculo de la edad para definir la tarifa
if int(edad) <12:
    print(f"tarifa infantil: {3.00}")
elif int(edad) <59:
    print(f"tarifa regular: {5.00}")
else:
    print(f"tarifa especial: {2.00}")