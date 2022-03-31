import main
from cgitb import text
from tkinter import * # Importamos libreria 

ventana = Tk()
ventana.title('Controles')
ventana.geometry('600x500')
ventana.resizable(False, False)
lb = Label(text= 'W => Adelante', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=10,y=0)
lb2 = Label(text= 'S => Atras', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=0,y=50)
lb3 = Label(text= 'A => Izquierda', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=9,y=100)
lb4 = Label(text= 'D => Derecha', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=7,y=150)
lb5 = Label(text= 'E => Rotación derecha', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=300,y=0)
lb6 = Label(text= 'Q => Rotación izqueirda', fg = 'blue', font = ('Liberation Serif', 8), width = 20, height = 2).place(x=303,y=50)

teclaW = Button(text = "W", width = 5, height = 2, command=main.movimiento('W')).place(x = 250, y = 300)
teclaS = Button(text = "S", width = 5, height = 2, command=main.movimiento('S')).place(x = 250, y = 300)
teclaD = Button(text = "D", width = 5, height = 2, command=main.movimiento('D')).place(x = 300, y = 300)
teclaA = Button(text = "A", width = 5, height = 2, command=main.movimiento('A')).place(x = 200, y = 300)
teclaE = Button(text = "E", width = 5, height = 2, command=main.movimiento('E')).place(x = 300, y = 300)
teclaQ = Button(text = "Q", width = 5, height = 2, command=main.movimiento('Q')).place(x = 200, y = 300)

ventana.mainloop()