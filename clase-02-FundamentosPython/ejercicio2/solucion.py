nombreApellido = input("Nombre y apellido: ").strip().capitalize()
edad = int(input("Edad: "))
promedio = int(input("Promedio académico: "))
ingresoMensual = int(input("Ingreso mensual del grupo familiar: "))
cantidadMateriasAprobadas = int(input("Cantidad de materias aprobadas: "))
esEstudianteRegular = input("Actualmente es estudiante regular (`SI` o `NO`): ").upper()

# Cumple requisitos de la beca si:
""" 
* Tener entre 18 y 30 años inclusive.
* Tener un promedio igual o superior a 7.
* Tener un ingreso familiar inferior a $1.500.000.
* Tener al menos 10 materias aprobadas.
* Ser estudiante regular. 
"""
cumpleRequisitoEdad = edad >= 18 and edad <= 30
cumpleRequisitoPromedio = promedio >= 7
cumpleRequisitoIngresoFamiliar = ingresoMensual < 1500000
cumpleRequisitoMaterias = cantidadMateriasAprobadas >= 10
cumpleRequisitoRegularidad = esEstudianteRegular == "SI"

print(
    f"Datos principales - Nombre: {nombreApellido}, Edad: {edad}, Promedio: {promedio}, Ingreso mensual: {ingresoMensual} y Es alumno regular: {esEstudianteRegular}"
)
print(f"Cumple el requisito de edad? {cumpleRequisitoEdad}")
print(
    f"Cumple el requisito academico: {cumpleRequisitoPromedio and cumpleRequisitoIngresoFamiliar and cumpleRequisitoMaterias and cumpleRequisitoRegularidad}"
)
