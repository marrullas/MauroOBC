class Alumno():
    nombre= None
    nota= None

    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def __str__(self):
        return f"nombre: {self.nombre}, nota: {self.nota}"

    def resultado(self):
        if(self.nota > 3):
            print ("El alumno ", self.nombre," aprobo con la nota: ", self.nota)
        else:
            print ("El alumno ", self.nombre," reprobo con la nota: ", self.nota)

a1 = Alumno("Magola", 2)

print(a1)

a1.resultado()