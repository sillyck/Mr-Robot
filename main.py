import serial
comando = 'cmd_vel[0.1,0,0]'
robot = serial.Serial('/dev/ttyACM0', 115200)

while True:
    
    key = input('Introduce un comando:  ')
    # print key
    if key == 'W':
        print("adelante")
        robot.write(comando.encode())
        robot.write('\n'.encode())
        
        variable = robot.readline()
        print (variable)
        # say what you got:
    else:
        print("detenido")
        robot.close()
        break
