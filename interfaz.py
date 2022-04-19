from tkinter import *
import tkinter 
import os

window = tkinter.Tk()
window.geometry("625x300")
window.resizable(False, False)

def obrir_manual():
    os.system('manual.py')

def obrir_automatic():
    os.system('automatic.py')

label = Label(window, text="Com vols moure el robot?")
label.pack(anchor=CENTER)
label.config(font=("Helvetica",24)) 

boto1 = tkinter.Button(window, text="Automatic", command=obrir_automatic).place(x=230, y=100)
boto2 = tkinter.Button(window, text="Manual", command=obrir_manual).place(x=330, y=100)

window.mainloop ()