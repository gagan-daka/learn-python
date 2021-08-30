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

#HERENCIA -> class 'nombreClasse'(clase a heredar):
class Trabajador(Persona):    
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa):
        super().__init__(nombre, edad, DNI) #esto hace referencia al metodo init de la classe Persona
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa

    def calcularSueldoAnual(self):
        self.pagaExtra = 2000
        return 12*self.sueldo + self.pagaExtra

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, universidad, curso, assignaturas):
        super().__init__(nombre, edad, DNI)
        self.universidad = universidad
        self.curso = curso
        self.assignaturas = assignaturas

    def describirse(self):
        print(f"""¡Hola soy {self.nombre}!. Tengo {self.edad} años y estudio en la universidad {self.universidad}.
        Estoy en el curso {self.curso}""")

trabajador = Trabajador("Juan", 33, "14785236Z", 1500, "machaca", "HeyHay")
trabajador.presentarse()
print(trabajador.DNI)
print(trabajador.calcularSueldoAnual())


estudiante = Estudiante("Ana", 21, "00000000Z", "UAB", 2, ["Cálculo", "Finanzas", "Álgebra"])
estudiante.describirse()
