import serial

robot = serial.Serial('/dev/ttyACM0', 115200)
comando = ('cmd_vel[0.1]')

def main(letra):
    while True:
        key = input('Introduce un comando:  ')
        robot.write(key.encode())
        # print key
        if key == 113:
            break
        elif key == 'W':
            print("adelante")
            functionMover()
        elif key == 97:
            print("izquierda")

        elif key == 115:
            print("atras")

        elif key == 100:
            print("derecha")

        else:
            print("detenido")

def functionMover():
    return comando