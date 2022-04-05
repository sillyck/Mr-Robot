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
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)

while True:
    if not robot.isOpen():
        robot.open()
    robot.write(sensor.encode())
    robot.write('\n'.encode())
    variable = robot.readline()
    varsens = variable.decode("utf-8")
    # archivo = open("sensores.txt", "r+")
    # archivo.write(varsens)
    # archivo.read()
    print(varsens)
    print("adelante")
    False
    robot.close()

