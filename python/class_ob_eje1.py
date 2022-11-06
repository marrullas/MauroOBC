class Vehiculo():
    color= "Rojo"
    Ruedas= 4
    Puertas= 5

    def __str__(self):
        return f"Color: {self.color} Puertas: {self.Ruedas} Ruedas: {self.Puertas}"

class Coche(Vehiculo):
    velocidad= 250
    Cilindrada= 300.5

    def __str__(self):
        return f"Color: {self.color} Puertas: {self.Ruedas} Ruedas: {self.Puertas} Velocidad: {self.velocidad} Cilindrada: {self.Cilindrada}"

c1 = Coche()
print(c1) 