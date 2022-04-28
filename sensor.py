from time import sleep
from tkinter import W
import serial
# Variables, velocidades del robot
delante = 'cmd_vel[0.1,0,0]'
delante2 = 'cmd_vel[0.02,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
atras2 = 'cmd_vel[-0.02,0,0]'
derecha = 'cmd_vel[0,0.1,0]'
derecha2 = 'cmd_vel[0,0.02,0]'
izquierda = 'cmd_vel[0,-0.1,0]'
izquierda2 = 'cmd_vel[0,-0.02,0]'
rot_der = 'cmd_vel[0,0,0.1]'
rot_iz = 'cmd_vel[0,0,-0.1]'
sensor = 'getSensors'
cont = 0
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)


while True:
    key = input('Introduce un comando:  ')

    if key == 'O' or key == 'o':
        print("Sensor")

        robot.write(sensor.encode())
        robot.write('\n'.encode())

    else:
        print("detenido")
        robot.close()
        break
    # Funcion para quitar mensajes.
    # if cont == 0:
    #     variable = robot.readline()
    #     variable = robot.readline()
    #     cont=1
    # if cont == 2:
    #     variable = robot.readline()
    #     cont = 1 
    # if cont == 1:
    #     variable = robot.readline()
    #     cont = 2
    variable = robot.readline()
    varsens = variable.decode("utf-8")
    
    print(varsens)
