from tkinter import *
import tkinter 
import os

ventana = tkinter.Tk()
ventana.geometry("625x300")
ventana.resizable(False, False)

def back():
    print("Atras")

def obrir_interfaz():
    ventana.destroy()
    os.system('interfaz.py')

boto1 = tkinter.Button(ventana, text="Automatic", command=back).place(x=275, y=125)
boto2 = tkinter.Button(ventana, text="Home", command=obrir_interfaz).place(x=0, y=0)

ventana.mainloop ()