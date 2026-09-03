# Actividad 2 - Ejercicio 7

cadena = '(5+3)*2")'

esExpresionValida = True
cantidadParentesisApertura = cadena.count("(")
cantidadParentesisClausura = cadena.count(")")
existeCaracterInvalido = cadena.find('"')
print(f"Cantidad parentesis que abren: {cantidadParentesisApertura}")
print(f"Cantidad parentesis que cierran: {cantidadParentesisClausura}")

if (
    cantidadParentesisApertura != cantidadParentesisClausura
    or existeCaracterInvalido == True
):
    print("Es una expresion invalida")
else:
    print("Es una expresion valida")
""" for caracter in cadena:
    if caracter == '"':
        esExpresionValida = False
        print("Es una expresion invalida porque tiene comilla doble")
    else:
        print("Es una expresion valida") """
