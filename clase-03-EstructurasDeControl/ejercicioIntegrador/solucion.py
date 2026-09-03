# Declaro y asigno variables
cantidadEstudiantes = int(input("Numero de estudiantes: "))
nombresAlumno = ""
notaFinal = 0
porcentajeAsistencia = 0
cantidadEstudiantesPromocionados = 0
cantidadEstudiantesRegulares = 0
cantidadEstudiantesLibres = 0
cantidadEstudiantesDesaprobados = 0
sumaNotas = 0
notaMasAlta = 0

for estudiante in range(cantidadEstudiantes):

    # Pido informacion de alumno
    nombresAlumno = input("Ingrese nombre de alumno: ")
    notaFinal = float(input("Ingrese nota: "))
    porcentajeAsistencia = int(input("Porcentaje asistencia: "))

    # Si la nota esta fuera del rango, la pido hasta que este dentro del rango
    while notaFinal < 0 or notaFinal > 10:
        notaFinal = float(input("Ingrese nota: "))

    print(f"Alumno ingresado: {nombresAlumno}")
    situacionAcademica = ""
    # Situacion academica
    if porcentajeAsistencia >= 75:
        if notaFinal >= 7:
            situacionAcademica = "Promocionado"
            cantidadEstudiantesPromocionados += 1
        elif notaFinal >= 4 and notaFinal < 7:
            situacionAcademica = "Regular"
            cantidadEstudiantesRegulares += 1
        else:
            situacionAcademica = "Desaprobado"
            cantidadEstudiantesDesaprobados += 1
    else:
        situacionAcademica = "Libre"
        cantidadEstudiantesLibres += 1

    print(f"Situacion academinca: {situacionAcademica}")

    # Calculos con nota
    sumaNotas += notaFinal
    if notaMasAlta < notaFinal:
        notaMasAlta = notaFinal

# Promocionado si obtuvo una nota igual o superior a 7
# y una asistencia igual o superior al 75%.

# Informe

# Cantidad total de estudiantes.
print(f"Cantidad de estudiantes: {cantidadEstudiantes}")

# Cantidad de estudiantes promocionados.
print(f"Cantidad de promocionados: {cantidadEstudiantesPromocionados}")

# Cantidad de estudiantes regulares.
print(f"Cantidad de regulares: {cantidadEstudiantesRegulares}")

# Cantidad de estudiantes libres.
print(f"Cantidad de libres: {cantidadEstudiantesLibres}")

# Cantidad de estudiantes desaprobados.
print(f"Cantidad de desaprobados: {cantidadEstudiantesDesaprobados}")

# Promedio
print(f"Promedio: {sumaNotas / cantidadEstudiantes}")

# Nota mas alta
print(f"Nota mas alta: {notaMasAlta}")
