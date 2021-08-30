'''
--- TUPLAS ---
CONJUNTOS ORDENADOS DE DATOS QUE NO SE PUEDEN MODIFICAR
'''
'''
miTupla = ("BarbaBlanca", "Gol D Roger", "Shanks", "Buggy")
print(miTupla)

print(f"La longitud de mi tupla es: {len(miTupla)}")

for piratas in miTupla:
    print(f"Pirata número {miTupla.index(piratas)}: {piratas}")
'''

'''
INDEXADO DE TUPLAS ( = QUE EN TUPLAS)
'''
'''
miTupla = ("BarbaBlanca", "Gol D Roger", "Shanks", "Buggy")
print(miTupla)

primerElemento = miTupla[0]
ultimoElemento = miTupla[-1]
subTupla = miTupla[1:3]

print(f"El primer pirata es {primerElemento}")
print(f"El ultimo pirata es {ultimoElemento}")
print(subTupla)
'''
'''
MODIFICAR TUPLAS 
NO PODEMOS MODIFICAR(NI ELIMINAR NI MODIFICAR ELEMENTOS) DIRECTAMENTE UNA TUPLA.
TRANSFORMAR UNA TUPLA A UNA LISTA Y VICEVERSA
'''

'''
miTupla = ("BarbaBlanca", "Gol D Roger", "Shanks", "Buggy")
#del miTupla[1]
#miTupla[1]="Monkey D Luffy"
miLista = list(miTupla)
print(miLista)
print(type(miLista))

miLista.append("Portgas D. ace")
print(miLista)

miTupla = tuple(miLista)
print(miTupla)
print(type(miTupla))
'''

'''
EMPAQUETAR Y DESEMPAQUETAR TUPLAS
ASSIGNAR CADA ELEMENTO DE UNA TUPLA A UNA VARIABLE DISTINTA
'''
'''
miTupla = ("BarbaBlanca", "Gol D Roger", "Shanks", "Buggy") 

#EMPAQUETAR ELEMENTOS
pirata1 = "Nico Robin"
pirata2 = "Nami"
piratas = (pirata1, pirata2)
print(piratas)

#DESEMPAQUETAR ELEMENTOS
    #FORMA 1
(p1, p2, p3, p4) = miTupla
print(f"Piratas: {p1}, {p2}, {p3}, {p4}")
    #FORMA 2
(p1, *piratasNuevos) = miTupla
print(p1)
print(piratasNuevos)

#CREAR UNA TUPLA APARTIR DE OTRA TUPLA
miTupla2 = miTupla + piratas
print(miTupla2)

(pir1, *varios, ultimoPirata) = miTupla2
print(pir1)
print(varios)
print(ultimoPirata)
'''

'''
--- LISTAS DE TUPLAS --- 
PODEMOS CREAR LISTAS CUYOS ELEMENTOS SEAN TUPLAS. DE ESTA FORMA, 
PODEMOS ITERAR SOBRE LAS DIVERSAS TUPLAS Y ADEMAS DESEMPAQUETAR
SUS ELEMENTOS
'''

comida = [("primero", "macarrones"), ("segundo", "pollo"), ("postre", "flan")]
print("El menu de hoy es: ")

for numero, plato in comida:
    print(f"{numero}: {plato}")

artistas = {1: "C.Tangana", 2:"Duki"}
elementos = artistas.items()
print(elementos)

for clave, valor in elementos:
    print(f"{clave}:{valor}")