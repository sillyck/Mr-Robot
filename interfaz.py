from cgitb import text
from tkinter import *
from tkinter import font

robot = Tk()

app_width = 1000
app_height = 500

screen_width = robot.winfo_screenwidth()
screen_height = robot.winfo_screenheight()

robot.geometry(f'{app_width}x{app_height}+{100}+{100}')

botonPIzquierda=Button(text="Manual", width=10, height=5)
botonPDerecha=Button(text="Automatico", width=10, height=5)

botonPIzquierda.grid(row=3, column=0)
botonPDerecha.grid(row=3, column=4)

robot.mainloop()