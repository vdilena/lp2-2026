numero = 1
numeroAnterior = 0
resultado = 1

for indice in range(1,22):
    print(f'Resultado: {numeroAnterior}')
    resultado = numero + numeroAnterior
    numeroAnterior = numero
    numero = resultado

