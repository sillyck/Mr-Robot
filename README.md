# Mr. Robot

## Proyecto Robot

Proyecto donde se programa el movimiento del robot con sensores


## Documentation

En este proyecto se programara un robot con 12 sensores, 8 de movimiento y 4 de proximidad.
El robot tiene 2 modos de funcionamiento, modo automatico donde sigue una linia negra (recta u curvas), y el otro modo
es manual, controlandolo con las teclas WASD y Q (rotación hacia la izquierda) E (rotación hacia la derecha).
El robot se conecta directamente al arduino con el puerto ttyACM0, con un baudi de 115200

#### Main.py
En este fichero esta programado el movimiento del robot manualmente. Es un codigo bastante sencillo, utilizamos los comandos
adelante, izquierda, etc. para moverlo. Utilizamos condiciones con if para redirigir el robot donde queramos, W= hacia adelante, S= atras, A= izquierda, D= derecha, E= rotar hacia la derecha, Q= rotar hacia la izquierda.

#### Automatico.py
En este fichero esta programado el movimiento del robot en automatico. El robot se mueve obteniendo los sensores con la varable sensors
(dentro tiene el comando que le envia al arduino (getSensors)) y los mete dentro de un array.
Al obtener estos sensores algunas veces envia unos mensajes molestos, estos los cambiamos por numeros -1 (no se utilizan en el codigo) y lo
asignamos dentro del array.
    
Hacemos las condiciones con if y elif para mover el robot dependiendo de que sensor este pillando en ese mismo instante.
Tambien tiene una funcion que hace pararse cuando encuentra un obstaculo de por medio.

### En progreso:
#### Interfaz.py, automatic.py, manual.py
Son ficheros donde esta programado una interfaz basica para cada modo que hay, el interfaz.py es la interfaz principal que sale
al ejecutar el codigo, este tiene 2 botones que redirige hacia la interfaz automatic.py y a manual.py.  

El fichero automatic.py es la interfaz del modo automatico, tiene un boton para apagar al robot y otro para volver a la interfaz principal.    
El fichero manual.py es la interfaz del modo manual, tiene botones con flechas para moverlo, hace lo mismo que con las teclas WASD.
