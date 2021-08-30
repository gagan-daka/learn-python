'''
PILARES DE LA PROGRAMACION ORIENTADA A OBTEJOS (P00)
- HERENCIA
- POLIMORFISMO
- ENCAPSULACIÓN
- ABSTRACCIÓN

AL CREAR METODOS(funciones) DENTRO DE LA CLASSE
SIEMPRE HAY QUE PASARLE EL 'SELF' POR ()
'''


class Camiseta:
    
    #CONSTRUCTOR
    def __init__(self, marca, precio, talla, color): 
        self.marca = marca
        self.precio =precio
        self.talla = talla
        self.color = color
        self.rebaja = False


    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebaja = True    

    def infoProducto(self):
        info = f"Descripción de la camiseta:\nMarca: {self.marca}\nPrecio: {self.precio:.2F}€\nTalla: {self.talla}\nColor: {self.color}"
        if self.rebaja:
            info += "\nESTE PRODUCTO ESTÁ REBAJADO"
        return info

#INSTANCIAMOS LA CLASSE
camiseta = Camiseta("Nike", 19.99, "S", "Lila")
camisetaAdidas = Camiseta("Adidas", 30, "M", "Negra")

print(camisetaAdidas.precio)
camisetaAdidas.aplicarDescuento(50)
print(camisetaAdidas.precio)

camiseta.aplicarDescuento(20)
print(camiseta.precio)

print(camiseta.infoProducto())
print("####################")
print(camisetaAdidas.infoProducto())
