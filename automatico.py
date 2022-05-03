import re
from time import sleep
from tkinter import W
from numpy import array
import serial

# Variables, velocidades del robot
delante = 'cmd_vel[0.06,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.008,0]'
izquierda = 'cmd_vel[0,-0.008,0]'
rot_der = 'cmd_vel[0,0,0.5]'
rot_iz = 'cmd_vel[0,0,-0.5]'
parar = 'cmd_vel[0,0,0]'
delder = 'cmd_vel[0.06,-0.1,0.6]'
deliz = 'cmd_vel[0.06,0.1,-0.6]'
der2 = 'cmd_vel[0,0.01,0]'
iz2 = 'cmd_vel[0,-0.01,0]'
sensor = 'getSensors'
cont = 0
bol = 0

# array_sensores_string= [0,0,0,0,0,0,0,0,0,0,0,0]
# array_sensores = [0,0,0,0,0,0,0,0,0,0,0,0]
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)
def sensores():
    robot.write(sensor.encode())
    robot.write('\n'.encode())


while True:
    cont=0
    # Recibimos la inforación del arduino y lo imprimimos por pantalla
    
    sensores()
    variable = robot.readline()
    # sensores()
    # variable = robot.readline()
    # sensores()
    # variable = robot.readline()
    
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
    #     breakk

    # Codigo para los sensores de movimiento
    if array_sensores[3] == 2500 and array_sensores[4] == 2500:
        robot.write(delante.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        print("adelante")
    elif array_sensores[3] == -1 or array_sensores[4] == -1:
        print("sigue")
    elif array_sensores[2] == 2500 and array_sensores[3] == 2500:
        robot.write(iz2.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        print("derecha")
    elif array_sensores[4] == 2500 and array_sensores[5] == 2500:
        robot.write(der2.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        print("izquierda")
    elif array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] == 2500:
        robot.write(delder.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        print("derecha")
    elif array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] == 2500:
        robot.write(deliz.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        print("izquierda")
    # if array_sensores[3] < 2500:
    #     robot.write(delder.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("derecha")
    #     robot.write(sensor.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
        
    # elif array_sensores[4] < 2500:
    #     robot.write(deliz.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("izquierda")

    
        
        
        
    
    


