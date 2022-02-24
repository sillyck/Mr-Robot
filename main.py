import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
    comando = input('Introduce un comando:  ')

    arduino.write(comando.encode())
