import tkinter
from tkinter import ttk

def resetseleccion(event):
    seleccionado.set(None)

window  = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

seleccionado = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Argentina', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='Alemania', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='Brasil', value='3', variable=seleccionado)
btn = tkinter.Button(window, text="Reset")

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

btn.grid(column=0, row=4, pady=5, padx=5)

btn.bind('<Button-1>', resetseleccion)


window.mainloop()