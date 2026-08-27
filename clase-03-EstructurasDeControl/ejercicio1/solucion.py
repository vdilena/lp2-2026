edad = int(input("Edad: "))

if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad <= 65:
    print("entre 18 y 65 años")
else:
    print("Es mayor de 65 años")
