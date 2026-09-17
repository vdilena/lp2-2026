# Ejercicio 6
Una materia guarda los resultados de sus estudiantes en un archivo llamado calificaciones.csv.  
El archivo contiene las siguientes columnas:
```
nombre,nota
Ana,8
Juan,5
Lucia,9
Pedro,ausente
Maria,7
```
El programa deberá leer la información utilizando el módulo csv.  
Crear funciones que permitan:
* Determinar si una calificación puede convertirse correctamente a un número.
* Calcular el promedio de una lista de notas.
* Determinar si una nota corresponde a un estudiante aprobado, considerando que se aprueba con 6 o más.

Durante la lectura del archivo, algunas calificaciones podrían contener valores que no puedan convertirse a número, como ausente. Estos casos deberán ser controlados para evitar que el programa finalice con un error.  
Una vez procesados los datos, informar:
* Cantidad total de registros leídos.
* Cantidad de calificaciones válidas.
* Promedio de las calificaciones válidas.
* Nombres de los estudiantes aprobados.
* Nombres de los estudiantes cuya calificación no pudo ser procesada.  

Para generar la lista de estudiantes aprobados, utilizar una list comprehension.
