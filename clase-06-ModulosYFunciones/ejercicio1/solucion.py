# Definimos la funcion
def getPromedio(lista):
    # listaNumerosFuncion = [1, 8, -2, 77, 3]
    cantidadElemLista = len(lista)
    sumatoriaElementosLista = 0
    for item in lista:
        sumatoriaElementosLista += item
    return sumatoriaElementosLista / cantidadElemLista


# Cargamos datos preliminares de la funcion
terminoPedir = "S"
listaNumeros = []
while terminoPedir == "S":
    elementoLista = int(input("Ingresar elemento de lista: "))
    listaNumeros.append(elementoLista)
    terminoPedir = input("Seguir agregando? S/N ").upper()

print(f"Lista precargada: {listaNumeros}")
# print(f"Valores lista preliminar: {listaNumerosFuncion}") # No pertenece a este scope
# Ejecutamos la funcion
print(f"Promedio: {getPromedio(listaNumeros)}")
