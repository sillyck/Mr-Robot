import re
from time import sleep
from tkinter import W
from numpy import array
import serial

# Variables, velocidades del robot
adelante = 'cmd_vel[0.04,0,0]'
atras = 'cmd_vel[-0.06,0,0]'
derecha = 'cmd_vel[0.02,0.005,0]'
derecha2 = 'cmd_vel[0,0.01,0]'
izquierda = 'cmd_vel[0.02,-0.005,0]'
izquierda2 = 'cmd_vel[0,-0.01,0]'
parar = 'cmd_vel[0,0,0]'
delder = 'cmd_vel[0.025,-0.015,0.16]'
deliz = 'cmd_vel[0.025,0.015,-0.16]'
sensor = 'getSensors'

fin = False

# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)

#Funcion para obtener los sensores
def sensores():
    robot.write(sensor.encode())
    robot.write('\n'.encode())
#Funcion para detectar obstaculos con los sensores de proximidad
def proximidad(): 
    if array_sensores[8] > 90 or array_sensores[9] > 90 or array_sensores[10] > 90 or array_sensores[11] > 90:
        robot.write(parar.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
    #Si los sensores detecta -1, no hace nada
    elif array_sensores[8] == -1 or array_sensores[9] == -1 or array_sensores[10] == -1 or array_sensores[11] == -1:
        print("")
        
#Funciones para el movimiento del robot
def aatras():
        robot.write(atras.encode())
        robot.write('\n'.encode())
        proximidad()

def adel():
        robot.write(adelante.encode())
        robot.write('\n'.encode())
        proximidad()
def ader():
        robot.write(derecha.encode())
        robot.write('\n'.encode())
        proximidad()
def aiz():
        robot.write(izquierda.encode())
        robot.write('\n'.encode())
        proximidad()
def ader2():
        robot.write(derecha2.encode())
        robot.write('\n'.encode())
        proximidad()
def aiz2():
        robot.write(izquierda2.encode())
        robot.write('\n'.encode())
        proximidad()
def adelder():
        robot.write(delder.encode())
        robot.write('\n'.encode())
        proximidad()
def adeliz():
        robot.write(deliz.encode())
        robot.write('\n'.encode())
        proximidad()

while True:

    # Recibimos la inforación del arduino y lo imprimimos por pantalla
    
    sensores()
    variable = robot.readline()
    
    
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

    if array_sensores[3] == 2500 and array_sensores[4] == 2500:
        adel()
        variable = robot.readline()
        fin = False
   
    elif array_sensores[0] == 2500:
        aiz2()
        variable = robot.readline()
        if array_sensores[0] == 2500 and  array_sensores[1] == 2500:
            adeliz()
            variable = robot.readline()

    elif array_sensores[7] == 2500:
        ader2()
        variable = robot.readline()
        if array_sensores[7] == 2500 and  array_sensores[6] == 2500:
            adelder()
            variable = robot.readline()

    elif array_sensores[4] == 2500 or array_sensores[5] == 2500:
        ader()
        variable = robot.readline()

    elif array_sensores[3] == 2500 or array_sensores[2] == 2500:
        aiz()
        variable = robot.readline()

    elif array_sensores[1] == 2500 and array_sensores[2] == 2500 or array_sensores[0] == 2500 and array_sensores[1] == 2500  or array_sensores[0] == 2500:
        adeliz()
        variable = robot.readline()

    elif array_sensores[6] == 2500 and array_sensores[5] == 2500 or array_sensores[7] == 2500 and array_sensores[6] == 2500 or array_sensores[7] == 2500:
        adelder()
        variable = robot.readline()
    
    elif array_sensores[1] == 2500 and array_sensores[2] == 2500 and array_sensores[0] == 2500 and array_sensores[3] == 2500  and array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] == 2500 or array_sensores[1] == 2500 and array_sensores[2] == 2500 and array_sensores[0] == 2500 and array_sensores[3] == 2500  and array_sensores[4] == 2500 and array_sensores[5] == 2500 or array_sensores[2] == 2500 and array_sensores[3] == 2500  and array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] == 2500:
        adel()
        variable = robot.readline()
    #Elif para detectar si es linia discontinua
    elif array_sensores[1] < 2000 and array_sensores[2] < 2000 and array_sensores[0] < 2000 and array_sensores[3] < 2000  and array_sensores[4] < 2000 and array_sensores[5] < 2000 and array_sensores[6] < 2000 and array_sensores[7] < 2000 and fin == False and array_sensores[3] != -1 and array_sensores[4] != -1:
        adel()
        variable = robot.readline()
        proximidad()
        print("f")
        if array_sensores[3] != 2500 and array_sensores[4] != 2500:
            aatras()
            variable = robot.readline()
            fin=True
            print("t")
