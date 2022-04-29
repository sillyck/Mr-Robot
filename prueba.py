from time import sleep
from tkinter import W
import tkinter
import serial


# Conexión a arduino
robot = serial.Serial('/dev/ttyACM0', 115200)
import os

#Moviment valors
delante = 'cmd_vel[0.1,0,0]'
atras = 'cmd_vel[-0.1,0,0]'
derecha = 'cmd_vel[0,0.1,0]'
izquierda = 'cmd_vel[0,-0.1,0]'
rot_der = 'cmd_vel[0,0,0.1]'
rot_iz = 'cmd_vel[0,0,-0.1]'


ventana = tkinter.Tk()
ventana.resizable(False, False)

def w():
    print("adelante")
    robot.write(delante.encode())
    robot.write('\n'.encode())

def back():
    ventana.destroy()
    os.system('interfaz.py')

window_width = 625
window_height = 300

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

ventana.geometry(f'{window_width}x{window_height}+{x}+{y}')

# photo = PhotoImage(file = "img/home.png")
# up = PhotoImage(file = "img/arriba.png")
# rightt = PhotoImage(file = "img/derecha.png")
# down = PhotoImage(file = "img/abajo.png")
# left = PhotoImage(file = "img/izquierda.png")
# rotateR = PhotoImage(file = "img/rotateR.png")
# rotateL = PhotoImage(file = "img/rotateL.png")

boto_home = tkinter.Button(ventana, command=back).place(x=0, y=0)
boto_up = tkinter.Button(ventana, command=w).place(x=290, y=163)
# boto_rightt = tkinter.Button(ventana, image = rightt, command=provisional).place(x=327, y=200)
# boto_down = tkinter.Button(ventana, image = down, command=provisional).place(x=290, y=200)
# boto_left = tkinter.Button(ventana, image = left, command=provisional).place(x=253, y=200)
# boto_rotateR = tkinter.Button(ventana, image = rotateR, command=provisional).place(x=327, y=163)
# boto_rotateL = tkinter.Button(ventana, image = rotateL, command=provisional).place(x=253, y=163)

ventana.mainloop ()