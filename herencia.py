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


class Trabajador(Persona):
    pass