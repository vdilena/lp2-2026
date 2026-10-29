# Problema 1 (Red de sensores ambientales) [Dataset usado](https://www.kaggle.com/datasets/datasetengineer/smart-farming-data-2024-sf24)
Se desea diseñar un sistema para administrar estaciones de monitoreo ambiental distribuidas en diferentes puntos de una ciudad.  
Cada estación de monitoreo posee un código, un nombre y una ubicación. Una estación puede tener instalados varios sensores, pero cada sensor se encuentra instalado en una sola estación a la vez.  
Los sensores pueden ser de temperatura, humedad o concentración de CO₂. Todos poseen:
* número de serie;
* estado activo/inactivo;
* fecha de última calibración;
* historial de mediciones.

Los sensores reciben una lectura cruda proveniente del dispositivo físico y deben convertirla en el valor correspondiente:
* el sensor de temperatura recibe la temperatura expresada en décimas de grado Celsius: 247 representa 24.7 °C;
* el sensor de humedad recibe la humedad expresada en décimas de porcentaje: 653 representa 65.3 %;
* el sensor de CO₂ recibe directamente la concentración expresada en ppm: 850 representa 850 ppm.

Antes de almacenar una medición, cada sensor debe comprobar que se encuentre activo y que el valor obtenido sea válido.  
Se consideran valores técnicamente válidos:
* temperatura: entre -50 °C y 60 °C;
* humedad: entre 0 % y 100 %;
* CO₂: mayor o igual que 0 ppm.

Cada lectura aceptada genera una Medición, donde se almacena el valor, unidad y fecha/hora.  
Además, determinados valores generan una Alerta ambiental:
* temperatura superior a 35 °C;
* humedad inferior a 30 % o superior a 80 %;
* CO₂ superior a 1000 ppm.

Las alertas inicialmente están abiertas y posteriormente pueden ser reconocidas y cerradas por un operador (que posee legajo, nombre y apellido).  
Cada sensor conserva su historial de mediciones. Una medición puede generar como máximo una alerta. La alerta queda asociada a la medición que la originó.  
Se deben poder hacer las siguientes operaciones:
* Se deben poder hacer las siguientes operaciones:
    * Agregar sensor: Debe incorporar un sensor a la estación solamente si no existe otro con el mismo número de serie. Además, debe registrar al sensor como instalado en esa estación.
    * Quitar sensor: Busca el sensor correspondiente a través del número de serie y lo elimina de la estación. El sensor deja de estar asociado a ella, pero el sensor continúa existiendo.
    * Buscar sensor: Devuelve el sensor correspondiente a través del número de serie o nulo si no existe.
    * Registrar lectura: Recibe el número de serie junto a la lectura y la fecha y hora, busca el sensor correspondiente y le delega la lectura. Tener en cuenta que la estación no sabe convertir temperaturas, humedades ni CO₂ y que el sensor debe estar activo para tomar la medición.
* El sensor debe:
    * Interpretar lectura: recibir la lectura cruda y convertirla al valor correspondiente según el tipo de sensor.
    * Comprobar que la medición está en rangos válidos
    * Informar si requiere una alerta en relación al valor recibido
    * Informar la unidad de medida.
    * Activarse y desactivarse
    * Calibrarse
* La medición debe poder:
    * Mostrar fecha y hora, además de los valores de la medición con su unidad de medida.
* La alerta debe poder:
    * Ser reconocida por un operador
    * Ser cerrada siempre que previamente haya sido reconocida.






