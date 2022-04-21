from tkinter import *
import tkinter 
import os

ventana = tkinter.Tk()
ventana.geometry("625x300")
ventana.resizable(False, False)

def auto():
    print("Automatic")

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

photo = PhotoImage(file = "home.png")

boto1 = tkinter.Button(ventana, text="Automatic", command=auto).place(x=275, y=125)
boto2 = tkinter.Button(ventana, image = photo, command=back).place(x=0, y=0)

ventana.mainloop ()