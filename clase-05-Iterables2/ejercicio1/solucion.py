# Desarrollar un diccionario que almacene el nombre y la edad de 5 personas.
personas = [
    {"nombre": "Carolina Gomez", "edad": 35},
    {"nombre": "Juan Perez", "edad": 29},
    {"nombre": "Mariela Ramirez", "edad": 27},
]

# El programa debe permitir que el usuario busque por nombre y le devuelva la edad de esa persona.
nombreABuscar = input("Nombre a buscar: ").strip()
noTerminoRecorrerLista = True
indice = 0
encontroPersona = False
while noTerminoRecorrerLista == True and encontroPersona == False:
    elementoLista = personas[indice]
    if elementoLista.get("nombre").upper().strip() == nombreABuscar.upper():
        # print(f"{elementoLista.get("nombre")} tiene {elementoLista.get("edad")}")
        encontroPersona = True
    indice += 1
    noTerminoRecorrerLista = indice < len(personas)

if encontroPersona == True:
    print(f"{elementoLista.get("nombre")} tiene {elementoLista.get("edad")}")
else:
    print(f"No se encontro a {nombreABuscar}")
