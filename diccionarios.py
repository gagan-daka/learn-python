'''
UN DICCIONARIO ES UN CONJUNTO DE ELEMENTOS
DICCIONARIO = {'clave':valor, 'clave':valor}
'''
'''
gagan = {"Nombre":"Gagandeep", "Edad":21, "Ciudad": "Barcelona", "Aficiones": ["Lectura", "Peliculas", "Videojuegos", "Salir con Amigos"]}
print(gagan)

ana = {"Nombre": "Ana", "Edad": 25, "Ciudad": "Madrid", "Aficiones": ["Lectura", "Natacion", "Escritura", "Cantar"]}
print(ana)

trabajadores = {0: gagan, 1: ana}
print(trabajadores)

print(f"La longitus del diccionario de 'gagan' es: {len(gagan)}")
print(f"La longitus del diccionario de 'ana' es: {len(ana)}")
print(f"La longitus del diccionario de 'trabajadores' es: {len(trabajadores)}")

print("Ejemplo: claves duplicadas")
a = {"año":1999, "año":2001} #cuando tiene claves repetidas nos devuelve el ultimo elemento 'clave':'valor'
print(a)
'''

'''
#AÑADIR, ELIMINAR Y MODIFICAR ELEMENTOS DE UN DICCIONARIO
#UPDATE-> SI EXISTE LO ACTUALIZA, SI NO EXISTE LO CREA
gagan = {"Nombre":"Gagandeep", "Edad":18, "Ciudad": "Barcelona", "Aficiones": ["Lectura", "Peliculas", "Videojuegos", "Salir con Amigos"]}
print("Diccionario original: ")
print(gagan)

#AÑADIR
print("Añadir elementos: ")
gagan["cargo"] = ["CEO"]
print(gagan)

gagan.update({"sueldo":10000, "vacaciones":25})
print(gagan)

#ELIMINAR
print("Eliminar elementos: ")
del gagan["vacaciones"]
valorElementoEliminado = gagan.pop("cargo")
print(gagan)
print(f"El valor eliminado es: {valorElementoEliminado}")

print("Acceder a un elemento de un diccionario")
edad = gagan["Edad"] #la clave tiene que coincidir
print(f"Gagan tiene {edad} años")

#MODIFICAR ELEMENTOS
gagan["Edad"] = 20
gagan.update({"Ciudad": "Boston"})
print(gagan)
'''

'''
Buscador de productos. Tenemos varios productos, el usuario
mediante el nombre de un producto puede consultar su precio y sus unidades
en stock.
'''

'''
pantalones = {
    "nombre": "pantalones",
    "precio": 19.99,
    "cantidad": 5
}

chaquetas = {
    "nombre": "chaquetas",
    "precio": 59.99,
    "cantidad": 3
}

bufandas = {
    "nombre": "bufandas",
    "precio": 4.99,
    "cantidad": 1
}

productos = [
    pantalones,
    chaquetas, 
    bufandas
]

def askForInfo(nombreProducto):
    for producto in productos:
        if(producto["nombre"] == nombreProducto):
            return producto["precio"], producto["cantidad"]
            break
    else:
        return 0, 0

nombre = input("¿Qué producto estás buscando? -> ")    
precio, cantidad = askForInfo(nombre)
if precio == 0 and cantidad == 0:
    print("No existe dicho producto")
else:
    print(f"El producto {nombre} vale {precio}€ disponemos de {cantidad} unidades")
'''    

#ITERAR SOBRE VARIAS LISTAS A LA VEZ
ana = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "aficiones": ["Lectura", "Natacion", "Escritura", "Cantar"]}
#METODO 1
    #zip()-> va devolviendo pares de valores 
for clave, valor in zip(ana.keys(), ana.values()):
    print(f"{clave} -> {valor}")

#METODO 2    
for clave, valor in ana.items():
    print(f"{clave}:{valor}")