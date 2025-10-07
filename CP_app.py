# variables sueldos:
vendedor = input("Ingresa nombre del vendedor:")
sueldo_base = input ("ingresa sueldo base:")
ventas_mes = input ("Ventas mes:")
porcentaje_comision = 0.08
porcentaje_impuesto = 0.08

#calculamos comision base
comision_base = float(ventas_mes) * float(porcentaje_comision)

if float(ventas_mes) > 8000:
    bono = 300
else:
    bono= 0

impuesto = (float(comision_base) + float(bono)) * float(porcentaje_impuesto)
sueldo_final = float(sueldo_base) + float(comision_base) + float(bono) - float(impuesto)

print(f"reporte para: {vendedor}")
print(f"sueldo base : {sueldo_base}")
print(f"ventas del mes: {ventas_mes}")
print(f"+ comision (8%): S/ {comision_base}")
print(f"+ bono: S/ {bono}")
print(f"- impuesto (8%): S/ {impuesto:.2f}")
print(f"sueldo final neto: {sueldo_final}")

