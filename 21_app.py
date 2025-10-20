# Ejercicio 3 - Funciones

"""
Calcula el precio final de un producto aplicando un descuento.
El usuario debe ingresar un monto y un valor de porcentaje de descuento.
Por ejemplo: Un producto cuesta 2500 y el porcentaje de descuento es 10%
¿Cuanto es el monto a pagar?
"""

# Función para calcular monto pago
def calcularMonto(precio, descuento):
    montoDescuento = precio * (descuento/100)
    montoPago = precio - montoDescuento
    return montoPago

# Utilizando la función
precio = 5000
descuento = 5

montoPago = calcularMonto(precio, descuento)
print(f"El precio del producto es: S/. {precio}")
print(f"El porcentage de descuento es: {descuento}%")
print(f"El monto a pagar es: S/. {montoPago:.2f}")