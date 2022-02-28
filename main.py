import serial
led=0
variable= False
arduino = serial.Serial('/dev/ttyACM0', 9600)
def show():
    if led==1:
        print('****************'
              'Opciones:'
              '****************'
              'W = Mover hacia delante'
              'D = Rotar a la derecha'
              'S = Mover hacia atras'
              'A = Rotar a la izquierda')
    else:
        print('****************'
              'L = Encender led'
              'X = Salir')
while True:
    show();
    comando = input('Introduce un comando:  ')
    arduino.write(comando.encode())
    while variable != True:
        if comando == 'X':
            print("Saliendo")
            variable= True
        elif comando == 'W':
            print("Moviendose hacia delante")
        elif comando == 'S':
            print("Moviendose hacia atras")
        elif comando == 'D':
            print("Rotando hacia la derecha")
        elif comando == 'A':
            print("Rotando hacia la izquierda")
        elif comando == 'L':
            print("Led encendida")
        arduino.close();