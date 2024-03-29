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
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)


while True:
    key = input('Introduce un comando:  ')

    if key == 'W' or key == 'w':
        print("adelante")
        # Envia al arduino el comando cmd_vel
        robot.write(delante.encode())
        robot.write('\n'.encode()) #Ponemos \n (asignamos nueva linia para que no se junte con el siguiente comando y no de error)
    

    elif key == 'S' or key == 's':
        print("atras")

        robot.write(atras.encode())
        robot.write('\n'.encode()) 


    elif key == 'D' or key == 'd':
        print("derecha")

        robot.write(derecha.encode())
        robot.write('\n'.encode()) 

    elif key == 'A' or key == 'a':
        print("izquierda")

        robot.write(izquierda.encode())
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

    varsens = variable.decode("utf-8")
    
    print(varsens)
    sleep(1)