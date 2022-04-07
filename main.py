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

# def funcion_Sensor():
#     robot.write(sensor.encode())
#     robot.write('\n'.encode())
#     # Funcion para quitar mensajes.
#     if cont == 0:
#         variable = robot.readline()
#         variable = robot.readline()
#         cont=1
#     if cont == 2:
#         variable = robot.readline()
#         cont = 1 
#     if cont == 1:
#         variable = robot.readline()
#         cont = 2
#     varsens = variable.decode("utf-8")
#     # archivo = open("sensores.txt", "r+")
#     # archivo.write(varsens)
#     # archivo.read()
#     print(varsens)   

while True:
    key = input('Introduce un comando:  ')

    if key == 'W' or key == 'w':
        print("adelante")
        # Envia al arduino el comando cmd_vel
        robot.write(delante.encode())
        robot.write('\n'.encode()) #Ponemos \n (asignamos nueva linia para que no se junte con el siguiente comando y no de error)
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
        # archivo = open("sensores.txt", "r+")
        # archivo.write(varsens)
        # archivo.read()
        print(varsens)
    elif key == 'S' or key == 's':
        print("atras")

        robot.write(atras.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'D' or key == 'd':
        print("derecha")

        robot.write(derecha.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'A' or key == 'a':
        print("izquierda")

        robot.write(izquierda.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'E' or key == 'e':
        print("Rotando hacia la derecha")

        robot.write(rot_der.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'Q' or key == 'q':
        print("Rotando hacia la izquierda")

        robot.write(rot_iz.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    else:
        print("detenido")
        # robot.close()
        break
