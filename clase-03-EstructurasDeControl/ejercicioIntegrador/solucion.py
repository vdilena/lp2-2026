cantidadEstudiantes = int(input("Numero de estudiantes: "))
nombresAlumnos = ""
notaFinal = 0
porcentajeAsistencia = 0

for estudiante in range(cantidadEstudiantes):
    notaFinal = int(input("Ingrese nota: "))
    porcentajeAsistencia = int(input("Porcentaje asistencia: "))
    while (notaFinal < 0 or notaFinal > 10):
        notaFinal = int(input("Ingrese nota: "))

    # Promocionado si obtuvo una nota igual o superior a 7 
    # y una asistencia igual o superior al 75%.
    if porcentajeAsistencia >= 75:
        if notaFinal >= 7:
            print("Promocionado")
        elif notaFinal >= 4 and notaFinal < 7:
            print("Regular")
    elif porcentajeAsistencia < 75:
        print("Libre")
    else:
        print("Desaprobado")

    

# Promocionado si obtuvo una nota igual o superior a 7 
# y una asistencia igual o superior al 75%.


# Cantidad total de estudiantes.
print(cantidadEstudiantes)

# Cantidad de estudiantes promocionados.
