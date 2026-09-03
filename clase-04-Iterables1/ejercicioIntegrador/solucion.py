ventas = []
sigueAgregandoNumeros = "S"
while sigueAgregandoNumeros == "S":
    ventas.append(float(input("Ingresar valor de la venta: ")))
    sigueAgregandoNumeros = input("Quiere seguir ingresando? S/N: ").upper()

# La cantidad de ventas realizadas
cantidadVentas = len(ventas)
print(f"Cantidad de ventas: {cantidadVentas}")

# La recaudación total.
recaudacion = sum(ventas)
print(f"Recaudacion: {recaudacion}")

# El importe promedio de las ventas
promedio = recaudacion / cantidadVentas
print(f"Promedio de ventas { promedio }")

# La mediana de ventas??
# La moda de las ventas??

# La venta de mayor importe.
print(f"Venta de mayor importe: {max(ventas)}")

# La venta de menor importe.
print(f"Venta de menor importe: {min(ventas)}")

# Cuántas ventas superaron el promedio diario.
ventasSuperanPromDiario = 0
importesQueSuperanPromedio = []
ventasImportantes = []
ventasPocoImportantes = []
ventasImportantesYPocoImportantes = []
for venta in ventas:
    if venta > promedio:
        ventasSuperanPromDiario += 1
        # Los importes que superaron dicho promedio.
        importesQueSuperanPromedio.append(venta)

    # Ventas importantes
    if venta == 50000 or venta == 100000 or venta == 200000:
        print(f"El importe {venta} determina que es una venta importante!")
        ventasImportantes.append(venta)
    elif venta < 20000:
        print(f"El importe {venta} determina que es una venta poco importante!")
        ventasPocoImportantes.append(venta)

print(f"Cantidad de ventas que superan el promedio: {ventasSuperanPromDiario}")
print(importesQueSuperanPromedio)

# Ordenar las ventas del mayor a menor precio
ventas.sort(reverse=True)
print(ventas)
ventasImportantesYPocoImportantes = ventasImportantes + ventasPocoImportantes
print(f"Ventas importantes y poco importantes: {ventasImportantesYPocoImportantes}")


# print(ventas)
