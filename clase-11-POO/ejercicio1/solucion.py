from abc import ABC, abstractmethod
from enum import Enum
from datetime import date, datetime
import pandas as pd
from pathlib import Path


class EstadoAlerta(Enum):
    ABIERTA = "ABIERTA"
    RECONOCIDA = "RECONOCIDA"
    CERRADA = "CERRADA"


class TipoSensor(Enum):
    TEMPERATURA = "TEMPERATURA"
    HUMEDAD = "HUMEDAD"
    CO2 = "CO2"


class Ubicacion:
    def __init__(self, calle: str, numero: int, provincia: str):
        self._calle = calle
        self._numero = numero
        self._provincia = provincia

    @property
    def calle(self):
        return self._calle

    @calle.setter
    def calle(self, calle):
        self._calle = calle

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def provincia(self):
        return self._provincia

    @provincia.setter
    def provincia(self, provincia):
        self._provincia = provincia

    def obtenerDireccion(self) -> "Ubicacion":
        pass

    def __str__(self):
        return f"(Calle : {self._calle}, Numero: {self._numero} y provincia: {self._provincia})"


class Estacion:
    def __init__(self, codigo: str, nombre: str, ubicacion: Ubicacion):
        self._codigo = codigo
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._sensores = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @property
    def sensores(self):
        return self._sensores

    @sensores.setter
    def sensores(self, sensores):
        self._sensores = sensores

    def agregarSensor(self, sensor: "Sensor") -> bool:
        pass

    def quitarSensor(self, numeroSerie: str) -> bool:
        pass

    def buscarSensor(self, numeroSerie: str) -> "Sensor":
        pass

    def registrarLectura(
        self, numeroSerie: str, lectura: int, fechaHora: datetime
    ) -> "Medicion":
        pass

    def __str__(self):
        return f"La estacion esta compuesta por Codigo: {self._codigo}, Nombre: {self._nombre} y ubicacion: {self._ubicacion}"


class Sensor(ABC):
    def __init__(self, numeroSerie: str, activo: bool, fechaUltimaCalibracion: date):
        self._numeroSerie = numeroSerie
        self._activo = activo
        self._fechaUltimaCalibracion = fechaUltimaCalibracion
        self._estacion = None
        self._mediciones = []

    @property
    def numeroSerie(self):
        return self._numeroSerie

    @numeroSerie.setter
    def numeroSerie(self, numeroSerie):
        self._numeroSerie = numeroSerie

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    def get_fechaUltimaCalibracion(self):
        return self._fechaUltimaCalibracion

    def set_fechaUltimaCalibracion(self, fecha):
        self._fechaUltimaCalibracion = fecha

    @property
    def estacion(self):
        return self._estacion

    @estacion.setter
    def estacion(self, estacion):
        self._estacion = estacion

    @property
    def mediciones(self):
        return self._mediciones

    @mediciones.setter
    def mediciones(self, mediciones):
        self._mediciones = mediciones

    def registrarLectura(self, lectura: int, fechaHora: datetime) -> "Medicion":
        pass

    def activar(self) -> None:
        pass

    def desactivar(self) -> None:
        pass

    def calibrar(self, fecha: date) -> None:
        pass

    @abstractmethod
    def interpretarLectura(self, lectura: int) -> float:
        pass

    @abstractmethod
    def esValorValido(self, valor: float) -> bool:
        pass

    @abstractmethod
    def requiereAlerta(self, valor: float) -> bool:
        pass

    @abstractmethod
    def obtenerUnidad(self) -> str:
        pass

    def __str__(self):
        return f"Tipo de sensor: {self._numeroSerie}"

    @abstractmethod
    def mostrarDetalleMedicion(self):
        pass


class SensorTemperatura(Sensor):
    def interpretarLectura(self, lectura: int) -> float:
        pass

    def esValorValido(self, valor: float) -> bool:
        pass

    def requiereAlerta(self, valor: float) -> bool:
        pass

    def obtenerUnidad(self) -> str:
        pass

    def mostrarDetalleMedicion(self):
        for medicion in self._mediciones:
            print(f"Valor: {medicion.valor} C")


class SensorHumedad(Sensor):
    def interpretarLectura(self, lectura: int) -> float:
        pass

    def esValorValido(self, valor: float) -> bool:
        pass

    def requiereAlerta(self, valor: float) -> bool:
        pass

    def obtenerUnidad(self) -> str:
        pass

    def mostrarDetalleMedicion(self):
        for medicion in self._mediciones:
            print(f"Valor: {medicion.valor} %")


class SensorCO2(Sensor):
    def interpretarLectura(self, lectura: int) -> float:
        pass

    def esValorValido(self, valor: float) -> bool:
        pass

    def requiereAlerta(self, valor: float) -> bool:
        pass

    def obtenerUnidad(self) -> str:
        pass

    def mostrarDetalleMedicion(self):
        for medicion in self._mediciones:
            print(f"Valor: {medicion.valor} ppm")


class Medicion:
    def __init__(self, valor: float, unidad: str, fechaHora: datetime, sensor: Sensor):
        self._valor = valor
        self._unidad = unidad
        self._fechaHora = fechaHora
        self._sensor = sensor
        self._alerta = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def unidad(self):
        return self._unidad

    @unidad.setter
    def unidad(self, unidad):
        self._unidad = unidad

    @property
    def fechaHora(self):
        return self._fechaHora

    @fechaHora.setter
    def fechaHora(self, fechaHora):
        self._fechaHora = fechaHora

    @property
    def sensor(self):
        return self._sensor

    @sensor.setter
    def sensor(self, sensor):
        self._sensor = sensor

    @property
    def alerta(self):
        return self._alerta

    @alerta.setter
    def alerta(self, alerta):
        self._alerta = alerta

    def mostrarDetalle(self) -> str:
        pass


class Alerta:
    def __init__(self, estado: EstadoAlerta, medicion: Medicion):
        self._estado = estado
        self._medicion = medicion
        self._operador = None

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def medicion(self):
        return self._medicion

    @medicion.setter
    def medicion(self, medicion):
        self._medicion = medicion

    @property
    def operador(self):
        return self._operador

    @operador.setter
    def operador(self, operador):
        self._operador = operador

    def reconocer(self, operador: "Operador") -> None:
        pass

    def cerrar(self, operador: "Operador") -> None:
        pass


class Operador:
    def __init__(self, legajo: str, nombre: str, apellido: str):
        self._legajo = legajo
        self._nombre = nombre
        self._apellido = apellido
        self._alertas = []

    @property
    def legajo(self):
        return self._legajo

    @legajo.setter
    def legajo(self, legajo):
        self._legajo = legajo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def alertas(self):
        return self._alertas

    @alertas.setter
    def alertas(self, alertas):
        self._alertas = alertas


if __name__ == "__main__":

    ubicacion1 = Ubicacion("Corrientes", 1500, "Buenos Aires")
    estacion1 = Estacion("EST001", "Estación Centro", ubicacion1)
    print(ubicacion1.calle, estacion1.nombre)

    carpeta = Path(__file__).resolve().parent

    # Inicializacion de dataframes
    df_estaciones = pd.read_csv(carpeta / "estaciones.csv")
    df_sensores = pd.read_csv(carpeta / "sensores.csv")
    df_mediciones = pd.read_csv(carpeta / "mediciones.csv")
    df_operadores = pd.read_csv(carpeta / "operadores.csv")

    # Prueba de obtencion de datos
"""     print(df_estaciones.head())
    print(df_sensores.head())
    print(df_mediciones.head())
    print(df_operadores.head())
    print(f"Primera fila de mediciones: {df_mediciones.iloc[0]}")
    print(f"Primera fila de mediciones, valor numero de serie: {df_mediciones.iloc[0]["numeroSerie"]}") """

# Cargar los objetos

estaciones = []
for indice, fila in df_estaciones.iterrows():
    # print(f"Estacion: {fila["nombre"]}")
    ubicacion = Ubicacion(fila["calle"], fila["numero"], fila["provincia"])
    estacion = Estacion(fila["codigo"], fila["nombre"], ubicacion)
    estaciones.append(estacion)

for est in estaciones:
    print(est)

sensores = []
for indice, fila in df_sensores.iterrows():

    sensor = None
    if fila["tipo"] == TipoSensor.TEMPERATURA.name:
        sensor = SensorTemperatura(
            fila["numeroSerie"], fila["activo"], fila["fechaUltimaCalibracion"]
        )
    elif fila["tipo"] == TipoSensor.HUMEDAD.name:
        sensor = SensorHumedad(
            fila["numeroSerie"], fila["activo"], fila["fechaUltimaCalibracion"]
        )
    else:
        sensor = SensorCO2(
            fila["numeroSerie"], fila["activo"], fila["fechaUltimaCalibracion"]
        )
    sensores.append(sensor)

for indice, fila in df_mediciones.iterrows():

    valor = fila["valor"]
    unidad = fila["unidad"]
    fechaHora = fila["fechaHora"]
    medicion = Medicion(valor, unidad, fechaHora, sensor)

    numeroSerieMedicion = fila["numeroSerie"]
    for sensor in sensores:
        if sensor.numeroSerie == numeroSerieMedicion:
            sensor.mediciones.append(medicion)
            # print(sensor.numeroSerie)
            break

# Muestro los valores de las mediciones
for sensor in sensores:
    sensor.mostrarDetalleMedicion()
