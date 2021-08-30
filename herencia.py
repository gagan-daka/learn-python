class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
    def presentarse(self):
        print(f"¡Hola! me llamo {self.nombre} y tengo {self.edad} años")

gagan = Persona("Gagan", 21, "12345678X")
gagan.presentarse()
print(gagan.DNI)

#HERENCIA
class Trabajador(Persona):
    pass

trabajador = Trabajador("Juan", 33, "14785236Z")
trabajador.presentarse()
print(trabajador.DNI)