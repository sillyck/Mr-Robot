from tkinter import *
import tkinter 
import os

window = tkinter.Tk()
window.geometry("625x300")
window.resizable(False, False)

def obrir_manual():
    window.destroy()
    os.system('manual.py')

def obrir_automatic():
    window.destroy()
    os.system('automatic.py')
    
label = Label(window, text="Com vols moure el robot?")
label.pack(anchor=CENTER)
label.config(font=("Helvetica",24)) 

window_width = 625
window_height = 300

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

boto1 = tkinter.Button(window, text="Automatic", command=obrir_automatic).place(x=230, y=100)
boto2 = tkinter.Button(window, text="Manual", command=obrir_manual).place(x=330, y=100)

window.mainloop ()