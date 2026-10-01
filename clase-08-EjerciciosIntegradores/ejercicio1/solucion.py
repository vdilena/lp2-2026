import random


def crearCuenta(numero, nombre, tipoCuenta, saldoInicial):
    return {
        "numero": numero,
        "nombre": nombre,
        "tipoCuenta": tipoCuenta,
        "saldo": saldoInicial,
    }


def pedirDatosParaCrearCuenta():

    print("Inicia el proceso de creacion de cuenta")

    numero = random.randint(100000, 999999)
    nombre = input("Nombre: ")

    tipoCuenta = input("Tipo de cuenta: COR/AHO --> ").upper()
    while tipoCuenta != "COR" and tipoCuenta != "AHO":
        tipoCuenta = input("Vuelva a ingvresar tipo de cuenta: COR/AHO --> ").upper()

    saldoInicial = 0
    if tipoCuenta == "COR":
        saldoInicial = 2000000
    else:
        saldoInicial = 3000000

    print("Finaliza el proceso de creacion de cuenta")
    return crearCuenta(numero, nombre, tipoCuenta, saldoInicial)


def buscarCuenta(numeroCuenta):
    cuentaEncontrada = None
    for cuenta in cuentas:
        # if numeroCuenta in cuenta.values()
        if numeroCuenta == cuenta.get("numero"):
            cuentaEncontrada = cuenta

    return cuentaEncontrada


def mostrarNumerosCuentas():
    for cuenta in cuentas:
        print(f"Cuenta nro: {cuenta["numero"]}")


def depositar():
    nroCuentaABuscar = int(input("Ingresa numero de cuenta: "))
    cuentaEncontrada = buscarCuenta(nroCuentaABuscar)
    if cuentaEncontrada != None:
        montoATransferir = input("Monto a transferir: ")
        while montoATransferir.isnumeric() == False:
            montoATransferir = input("Volver a ingresar monto a transferir: ")
        cuentaEncontrada["saldo"] += float(montoATransferir)
    else:
        print("No se encontro la cuenta")


# Creacion de cuentas bancarias
cuentas = []

sigaAgregaAgregandoCuentas = "SI"
while sigaAgregaAgregandoCuentas == "SI":
    cuentas.append(pedirDatosParaCrearCuenta())
    sigaAgregaAgregandoCuentas = input("Mas cuentas? SI/NO: ").upper()

print(f"Cuentas bancarias: {cuentas}")

# Depositos
mostrarNumerosCuentas()
depositar()
print(f"Cuentas bancarias: {cuentas}")
