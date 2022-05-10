import re
from time import sleep
from tkinter import W
from numpy import array
import serial

# Variables, velocidades del robot
delante = 'cmd_vel[0.03,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.005,0]'
derecha2 = 'cmd_vel[0,0.01,0]'
izquierda = 'cmd_vel[0,-0.005,0]'
izquierda2 = 'cmd_vel[0,-0.01,0]'
rot_der = 'cmd_vel[0,0,0.07]'
rot_iz = 'cmd_vel[0,0,-0.07]'
parar = 'cmd_vel[0,0,0]'
# delder = 'cmd_vel[0.03,-0.02,0.18]'
# deliz = 'cmd_vel[0.03,0.02,-0.18]'
delder = 'cmd_vel[0.025,-0.015,0.16]'
deliz = 'cmd_vel[0.025,0.015,-0.16]'
# delder = 'cmd_vel[0.05,-0.1,0.6]'
# deliz = 'cmd_vel[0.05,0.1,-0.6]'
sensor = 'getSensors'
x = 0.03
y = 0
z = 0
comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
cont = 0
bol = 0

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
        robot.write(delante.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
    
    elif array_sensores[0] == 2500:
        robot.write(izquierda2.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        if array_sensores[0] == 2500 and  array_sensores[1] == 2500:
            robot.write(deliz.encode())
            robot.write('\n'.encode())
            variable = robot.readline()

    elif array_sensores[7] == 2500:
        robot.write(derecha2.encode())
        robot.write('\n'.encode())
        variable = robot.readline()
        if array_sensores[7] == 2500 and  array_sensores[6] == 2500:
            robot.write(delder.encode())
            robot.write('\n'.encode())
            variable = robot.readline()

    elif array_sensores[4] == 2500:
        robot.write(derecha.encode())
        robot.write('\n'.encode())
        variable = robot.readline()

    elif array_sensores[3] == 2500:
        robot.write(izquierda.encode())
        robot.write('\n'.encode())
        variable = robot.readline()

    elif array_sensores[1] == 2500 and array_sensores[2] == 2500 or array_sensores[0] == 2500 and array_sensores[1] == 2500  or array_sensores[0] == 2500:
        robot.write(deliz.encode())
        robot.write('\n'.encode())
        variable = robot.readline()

    elif array_sensores[6] == 2500 and array_sensores[5] == 2500 or array_sensores[7] == 2500 and array_sensores[6] == 2500 or array_sensores[7] == 2500:
        robot.write(delder.encode())
        robot.write('\n'.encode())
        variable = robot.readline()





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
    # if array_sensores[3] == 2500 and array_sensores[4] == 2500 or array_sensores[3] == 2500 and array_sensores[2] != 2500  or array_sensores[4] == 2500 and array_sensores[5] != 2500:
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("adelante")

    # elif array_sensores[3] == -1 or array_sensores[4] == -1:
    #     print("sigue")

    # elif array_sensores[2] == 2500 and array_sensores[3] == 2500 and array_sensores[0] != 2500 and array_sensores[1] != 2500 or array_sensores[1] == 2500 and array_sensores[2] == 2500 and array_sensores[0] != 2500:
    #     robot.write(iz2.encode())
    #     # robot.write(deliz.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()

    #     print("derecha")
    #     # sensores()
    #     # variable = robot.readline()
    #     # print(array_sensores)

    #     if array_sensores[1] == 2500 and array_sensores[2] == 2500 and array_sensores[0] != 2500 and array_sensores[3] != 2500:
    #         robot.write(rot_iz.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("rotiz")
    # elif array_sensores[0] == 2500 and array_sensores[1] != 2500:
    #         robot.write(iz2.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("derecha6")

    #         robot.write(rot_iz.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("rotiz6")

    # elif array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] != 2500 and array_sensores[7] != 2500 or array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] != 2500:
    #     robot.write(der2.encode())
    #     # robot.write(delder.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()

    #     print("izquierda")
    #     # sensores()
    #     # variable = robot.readline()
    #     # print(array_sensores)

    #     if array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[4] != 2500 and array_sensores[7] != 2500:
    #         robot.write(rot_der.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("rotder")

    # elif array_sensores[7] == 2500 and array_sensores[6] != 2500:
    #         robot.write(der2.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("izquierda6")

    #         robot.write(rot_der.encode())
    #         robot.write('\n'.encode())
    #         variable = robot.readline()
    #         print("rotder6")

    # elif array_sensores[2] == 2500 and array_sensores[1] == 2500 and array_sensores[0] == 2500 or array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] == 2500 or array_sensores[1] == 2500 and array_sensores[0] == 2500 or array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] == 2500 and array_sensores[0] == 2500:
    #     robot.write(deliz.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("derechasi")

    #     # if array_sensores[3] != 2500 and array_sensores[4] != 2500:
    #     # # while array_sensores[3] != 2500 or array_sensores[4] != 2500:

    #     #     variable = robot.readline()
    #     #     print(array_sensores)
    #     #     robot.write(iz3.encode())
    #     #     robot.write('\n'.encode())
    #     #     variable = robot.readline()
    #     #     print("izquierda3")
        
    # elif array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] == 2500 or array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] == 2500 or array_sensores[6] == 2500 and array_sensores[7] == 2500 or array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] == 2500:
    #     robot.write(delder.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("izquierdasi")

    # if array_sensores[3] == 2500 and array_sensores[4] == 2500:
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("adelante")

    # elif array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] != 2500:
    #     x=0
    #     y=-0.005
    #     z=-0
    #     comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("iz")
    
    # elif array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] != 2500:
    #     x=0
    #     y=0.005
    #     z=0
    #     comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("der")
    

    # elif array_sensores[2] == 2500 and array_sensores[1] == 2500 and array_sensores[0] == 2500 or array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] == 2500 or array_sensores[1] == 2500 and array_sensores[0] == 2500 or array_sensores[3] == 2500 and array_sensores[2] == 2500 and array_sensores[1] == 2500 and array_sensores[0] == 2500:
    #     x= x + 0.02
    #     y= y + 0.02
    #     z= z - 0.1
    #     comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("derechasi")
    #     while array_sensores[3] == 2500 and array_sensores[4] == 2500:
    #         print("dentrowhile")
    #         if array_sensores[3] == 2500 and array_sensores[4] == 2500:
    #             print("dentroif")
    #             x= 0.05
    #             y= 0
    #             z= 0
    #             comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #             robot.write(comando.encode())
    #             robot.write('\n'.encode())
    #             variable = robot.readline()
    #             print("adelante")
    
    # elif array_sensores[4] == 2500 and array_sensores[5] == 2500 and array_sensores[6] != 2500 and array_sensores[7] != 2500 or array_sensores[5] == 2500 and array_sensores[6] == 2500 and array_sensores[7] != 2500:
    #     # x= 0.05
    #     # y= -0.04
    #     # z= 0.3
    #     x= x + 0.02
    #     y= y - 0.02
    #     z= z + 0.1
    #     comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #     robot.write(comando.encode())
    #     robot.write('\n'.encode())
    #     variable = robot.readline()
    #     print("izquierdasi")
    #     while array_sensores[3] == 2500 and array_sensores[4] == 2500:
    #         if array_sensores[3] == 2500 and array_sensores[4] == 2500:
    #             x= 0.05
    #             y= 0
    #             z= 0
    #             comando = 'cmd_vel['+str(x)+','+str(y)+','+str(z)+']'
    #             robot.write(comando.encode())
    #             robot.write('\n'.encode())
    #             variable = robot.readline()
    #             print("adelante")


        # if array_sensores[3] != 2500 and array_sensores[4] != 2500:
        #     # while array_sensores[3] != 2500 or array_sensores[4] != 2500:

        #     variable = robot.readline()
        #     print(array_sensores)

        #     robot.write(der3.encode())
        #     robot.write('\n'.encode())
        #     variable = robot.readline()
        #     print("derecha3")


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