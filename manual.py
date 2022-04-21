from tkinter import *
import tkinter 
import os
from turtle import right

ventana = tkinter.Tk()
ventana.geometry("625x300")
ventana.resizable(False, False)

def provisional():
    print("a")

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

photo = PhotoImage(file = "img/home.png")
up = PhotoImage(file = "img/arriba.png")
rightt = PhotoImage(file = "img/derecha.png")
down = PhotoImage(file = "img/abajo.png")
left = PhotoImage(file = "img/izquierda.png")
rotateR = PhotoImage(file = "img/rotateR.png")
rotateL = PhotoImage(file = "img/rotateL.png")

boto_home = tkinter.Button(ventana, image = photo, command=back).place(x=0, y=0)
boto_up = tkinter.Button(ventana, image = up, command=provisional).place(x=290, y=163)
boto_rightt = tkinter.Button(ventana, image = rightt, command=provisional).place(x=327, y=200)
boto_down = tkinter.Button(ventana, image = down, command=provisional).place(x=290, y=200)
boto_left = tkinter.Button(ventana, image = left, command=provisional).place(x=253, y=200)
boto_rotateR = tkinter.Button(ventana, image = rotateR, command=provisional).place(x=327, y=163)
boto_rotateL = tkinter.Button(ventana, image = rotateL, command=provisional).place(x=253, y=163)

ventana.mainloop ()