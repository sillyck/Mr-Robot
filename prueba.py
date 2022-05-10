import re
from time import sleep
from tkinter import W
import serial

# Variables, velocidades del robot
delante = 'cmd_vel[0.03,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.008,0]'
izquierda = 'cmd_vel[0,-0.008,0]'
rot_der = 'cmd_vel[0,0,0.5]'
rot_iz = 'cmd_vel[0,0,-0.5]'
parar = 'cmd_vel[0,0,0]'
delder = 'cmd_vel[0.05,0.04,0.4]'
deliz = 'cmd_vel[0.012,0,-0.16]'
del2 = 'cmd_vel[0.01,0,0]'
iz2 = 'cmd_vel[0.01,0,-0.1]'
der2 = 'cmd_vel[0.01,0,0.1]'
sensor = 'getSensors'
cont = 0
bol = 0
# array_sensores_string= [0,0,0,0,0,0,0,0,0,0,0,0]
# array_sensores = [0,0,0,0,0,0,0,0,0,0,0,0]
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)

while True:
    cont=0
    # Recibimos la inforación del arduino y lo imprimimos por pantalla
    robot.write(sensor.encode())
    robot.write('\n'.encode())
    
    # Funcion para quitar mensajes.
    if cont == 0:
        variable = robot.readline()
        cont = 1

    varsens = variable.decode("utf-8")
    #Pasamos el siguiente texto a un numero que no utilicemos solo para ponerlo en el array
    varsens = re.sub("Basic Encoder Test:", "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",varsens)
    varsens = re.sub("Message is Send by I2C", "-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1",varsens)
    varsens = re.sub("\\r|\\n", "",varsens) #Quitamos el \r y \n que se le añade al mensaje del sensor
    array_sensores_string=varsens.split(',') #Dividimos el mensaje y lo ponemos en el array
    # Convertimos el array string a int
    array_sensores = list(map(int, array_sensores_string))
    print(array_sensores)

    sleep(1)

    # Codigo para los sensores de proximidad 
    # if array_sensores[8] < 17 and array_sensores[9] < 13 and array_sensores[10] < 13 and array_sensores[11] < 17:
    #     robot.write(delante.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()

    # elif array_sensores[8] == -1 or array_sensores[9] == -1 or array_sensores[10] == -1 or array_sensores[11] == -1:
    #     print("")

    # elif array_sensores[8] > 200 or array_sensores[9] > 200 or array_sensores[10] > 200 or array_sensores[11] > 200:
    #     print("no")
    #     robot.close()
    #     break

    # Codigo para los sensores de movimiento
    key = input('Introduce un comando:  ')
    if key == 'W' or key == 'w':
        print("adelante")
        # Envia al arduino el comando cmd_vel
        robot.write(delder.encode())
        robot.write('\n'.encode())
    
        
        
    
    

