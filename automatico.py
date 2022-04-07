import re
from time import sleep
from tkinter import W

import serial
# Variables, velocidades del robot
delante = 'cmd_vel[0.1,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.1,0]'
izquierda = 'cmd_vel[0,-0.1,0]'
rot_der = 'cmd_vel[0,0,0.5]'
rot_iz = 'cmd_vel[0,0,-0.5]'
sensor = 'getSensors'
cont = 0
array_sensores_string= [0,0,0,0,0,0,0,0,0,0,0,0]
array_sensores = [0,0,0,0,0,0,0,0,0,0,0,0]
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)

while True:
    cont=0
    print("hola")
    # Recibimos la inforación del arduino y lo imprimimos por pantalla
    robot.write(sensor.encode())
    robot.write('\n'.encode())
    
    # Funcion para quitar mensajes.
    if cont == 0:
        variable = robot.readline()
        cont = 1
    # if cont == 1:
    #     variable = robot.readline()
    # variable = robot.readline()
    varsens = variable.decode("utf-8")
    varsens = re.sub("Basic Encoder Test:", "0",varsens)
    varsens = re.sub("\\r|\\n", "",varsens) #Quitamos el \r y \n que se le añade al mensaje del sensor
    array_sensores_string=varsens.split(',') #Dividimos el mensaje y lo ponemos en el array
    # array_sensores = [int(x) for x in array_sensores_string]
    array_sensores = list(map(int, array_sensores_string))
    print(array_sensores)
    sleep(1)
    # robot.close()

