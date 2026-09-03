indice = 0
numeros = []

# while(indice < 5):
for indice in range(5):
    numeroAIngresar = int(input("Ingresar un numero: "))
    numeros.append(numeroAIngresar)
    # indice +=1

# Imprimir la lista en su orden original.
print(numeros)

# Ordena la lista de manera ascendente y mostrarla.
numeros.sort()
print(numeros)

# Ordena la lista de manera descendente y mostrarla.
numeros.sort(reverse=True)
print(numeros)

# Cantidad de elementos de la lista
print(f"Cantidad de elementos: {len(numeros)}")

# Calcular la suma de todos los elementos de la lista
# cantidadElementosLista = sum(numeros)
# print(f"Suma de elementos: {cantidadElementosLista}")
sumatoria = 0
for numero in numeros:
    sumatoria += numero
print(f"Suma de elementos: {sumatoria}")

# Mostrar el número más grande y el más pequeño de la lista.
maximoDeLista = max(numeros)
minimoDeLista = min(numeros)
print(f"Maximo: {maximoDeLista} y minimo: {minimoDeLista}")
