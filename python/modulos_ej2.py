import time

horaActual = int(time.strftime("%H",time.localtime()))
if(horaActual > 19):
    print("Ya es hora de salir")
else:
    print("Aun te faltan ", 19 - horaActual, " horas para salir")