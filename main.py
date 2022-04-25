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

    if key == 'W' or key == 'w':
        print("adelante")
        # Envia al arduino el comando cmd_vel
        robot.write(delante.encode())
        robot.write('\n'.encode()) #Ponemos \n (asignamos nueva linia para que no se junte con el siguiente comando y no de error)
    
    elif key == '2' or key == '2':
        print("delante2")

        robot.write(delante2.encode())
        robot.write('\n'.encode()) 

    elif key == 'S' or key == 's':
        print("atras")

        robot.write(atras.encode())
        robot.write('\n'.encode()) 

    elif key == 'X' or key == 'x':
        print("atras")

        robot.write(atras2.encode())
        robot.write('\n'.encode()) 

    elif key == 'D' or key == 'd':
        print("derecha")

        robot.write(derecha.encode())
        robot.write('\n'.encode()) 
    elif key == 'C' or key == 'c':
        print("derecha2")

        robot.write(derecha2.encode())
        robot.write('\n'.encode())

    elif key == 'A' or key == 'a':
        print("izquierda")

        robot.write(izquierda.encode())
        robot.write('\n'.encode())
    elif key == 'Z' or key == 'z':
        print("izquierda2")

        robot.write(izquierda2.encode())
        robot.write('\n'.encode())

    elif key == 'E' or key == 'e':
        print("Rotando hacia la derecha")

        robot.write(rot_der.encode())
        robot.write('\n'.encode())

    elif key == 'Q' or key == 'q':
        print("Rotando hacia la izquierda")

        robot.write(rot_iz.encode())
        robot.write('\n'.encode())
    elif key == 'O' or key == 'o':
        print("Sensor")

        robot.write(sensor.encode())
        robot.write('\n'.encode())

    else:
        print("detenido")
        robot.close()
        break
# Recibimos la inforación del arduino y lo imprimimos por pantalla
    robot.write(sensor.encode())
    robot.write('\n'.encode())
    # Funcion para quitar mensajes.
    if cont == 0:
        variable = robot.readline()
        variable = robot.readline()
        cont=1
    if cont == 2:
        variable = robot.readline()
        cont = 1 
    if cont == 1:
        variable = robot.readline()
        cont = 2
    varsens = variable.decode("utf-8")

    print(varsens)
    sleep(1)