class Vehiculo():
    marca = None
    caballos = None
    color = "Rojo"

    def __init__(self, marca, caballos):
        self.marca = marca
        self.caballos = caballos

    def __str__(self) -> str:
        return f'Marca: {self.marca} Caballos: {self.caballos} Color: {self.color}'

import pickle

class UsarVehiculo():

    def crear(self, marca, caballos):
        f = open('auto.bin','wb')
        a1 = Vehiculo(marca, caballos)
        pickle.dump(a1, f)
        f.close()

    def leer(self):
        f = open('auto.bin','rb')        
        auto = pickle.load(f)
        f.close()
        print(auto)

us1 = UsarVehiculo()
us1.crear('BMW', 500)
us1.leer()