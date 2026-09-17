import csv
from pathlib import Path  # Se agrega la library pathlib para obtener el path absoluto

matrizEstudiantes = []

BASE_DIR = Path(__file__).resolve().parent
with open(
    BASE_DIR / "estudiantes.csv",
    mode="r",
) as csvEstudiantes:
    lineasArchivoLeido = csv.reader(csvEstudiantes, delimiter=",")
    matrizEstudiantes = list(lineasArchivoLeido)
    # print(matrizEstudiantes)

estudiantes = []
""" estudiantes = [
    {"nombre": "Ana", "edad": 22, "nota": 8},
    {"nombre": "Juan", "edad": 25, "nota": 6},
] """
# Recorro lista
claves = matrizEstudiantes[0]
# print(claves)
for item in matrizEstudiantes[1:]:
    estudiante = {claves[0]: item[0], claves[1]: int(item[1]), claves[2]: int(item[2])}
    estudiantes.append(estudiante)

    # Implementacion de lo pedido
    print(
        f"Nommbre y nota de cada estudiante: {estudiante["nombre"]} - {estudiante["nota"]}"
    )
cantidadEstudiamtes = len(estudiantes)
print(f"Cantidad total de estudiantes: {cantidadEstudiamtes}")

sumatoriaNotas = 0
estudiantesQueTuvieronMasDe7 = []
for est in estudiantes:
    sumatoriaNotas += est["nota"]
    if est["nota"] >= 7:
        estudiantesQueTuvieronMasDe7.append(est["nombre"])
print(f"Promedio: {sumatoriaNotas / cantidadEstudiamtes}")
print(f"Estudiantes que obtuvieron mas de 7: {estudiantesQueTuvieronMasDe7} ")

# print(f"Lista estudiantes: {estudiantes}")
# print(f"Elemento: {item}")
