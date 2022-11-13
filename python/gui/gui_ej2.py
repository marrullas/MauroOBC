import tkinter
from tkinter import ttk

def resetseleccion(event):
    seleccionado.set(None)

window  = tkinter.Tk()
#window.config(width=300, height=200)
window.geometry('500x250')
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)
window.title("Ejercicio 2 sección GUI")

seleccionado = tkinter.StringVar()

ttk.Label(window, text="Seleccione el campeón del mundial").grid(column=0, row=1, pady=5, padx=5)

seleccioncampeon = ttk.Combobox(window, width=27, textvariable=seleccionado)

seleccioncampeon['values'] = ('Argentina', 'Alemania', 'España', 'Brasil')

seleccioncampeon.grid(column=0, row=2, pady=5, padx=5)


window.mainloop()