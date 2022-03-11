import serial

# Variables, velocidades del robot
delante = 'cmd_vel[0.1,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.1,0]'
izquierda = 'cmd_vel[0,-0.1,0]'
rot_der = 'cmd_vel[0,0,0.5]'
rot_iz = 'cmd_vel[0,0,-0.5]'
# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)

while True:
    
    key = input('Introduce un comando:  ')
    # print keyW
    if key == 'W' | key == 'w':
        print("adelante")
        # Envia al arduino el comando cmd_vel
        robot.write(delante.encode())
        robot.write('\n'.encode()) #Ponemos \n (asignamos nueva linia para que no se junte con el siguiente comando y no de error)
        # Recibimos la inforación del arduino y lo imprimimos por pantalla
        variable = robot.readline()
        print (variable)
    elif key == 'S' | key == 's':
        print("atras")

        robot.write(atras.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'D' | key == 'd':
        print("derecha")

        robot.write(derecha.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'A' | key == 'a':
        print("izquierda")

        robot.write(izquierda.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'E' | key == 'e':
        print("Rotando hacia la derecha")

        robot.write(rot_der.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    elif key == 'Q' | key == 'q':
        print("Rotando hacia la izquierda")

        robot.write(rot_iz.encode())
        robot.write('\n'.encode()) 

        variable = robot.readline()
        print (variable)
    else:
        print("detenido")
        robot.close()
        break
