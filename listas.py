#REPASO DE CONCEPTOS BÁSICOS
'''
numeros = [1, 2, 3, 4, 5]
print(numeros)
primera_posicion = numeros[0]
longitud = len(numeros)
print(f"El primer valor es: {primera_posicion}\nLa longitud de la lista es: {longitud}")

#ITERAR SOBRE UNA LISTA
for num in numeros:
    print(num)

'''

'''
#INDEXADO Y SUBLISTAS
lista = ["El", "futur", "rei", "dels", "piratas"]
print(lista)
ultima_posicion = lista[-1]
print(ultima_posicion)
penultima_posicion = lista[-2]
print(penultima_posicion)

sublista = lista[1:5] #paramos en 5-1 = 4
print(sublista)
sublista = lista[:5]
print(sublista)
sublista = lista[1:]
print(sublista)
sublista = lista[-4:-1]
print(sublista)
'''
'''
#COMPROVAR SI UNA LISTA CONTIENE O NO UN ELEMENTO
lista = ["El", "futur", "rei", "dels", "piratas"]
palabra = "rei"
palabra_dos = "barbablanca"

if palabra in lista:
    print(f"La palabra '{palabra}' pertenece a la lista")

if palabra_dos not in lista:
    print(f"La palabra '{palabra_dos}' no está en la lista")
'''

'''
#MODIFICAR ELEMENTOS DE UNA LISTA
lenguajes = ["Python", "JavaScript", "C", "Java", "Kotlin", "Ruby", "SQL"]
print(lenguajes)
lenguajes[3] = "Angular"
print(lenguajes)
lenguajes[2] = lenguajes[2] + "++"
print(lenguajes)

lenguajes[2:4] = ["C#", "Laravel"]
print(lenguajes)

lenguajes[4:5] = ["PHP", "React", "Vue"]
print(lenguajes)
'''

'''
#METODOS DE LISTAS: AÑADIR ELEMENTOS
lenguajes = ["Python", "JavaScript", "C", "Java", "Kotlin", "Ruby", "SQL"]
print(lenguajes)

#INSERT()
lenguajes.insert(1, "C++")
print(lenguajes)

#APPEND()
lenguajes.append("C#") #agrega alfinal de la lista
print(lenguajes)

#EXTEND()
frutas = ["Fresa", "Peras", "Uvas"]
print(frutas)
frutas_extra = ["Mango", "Manzana", "Platano"]
frutas.extend(frutas_extra)
print(frutas)
print(frutas_extra)
'''

'''
#METODOS DE LISTAS: ELIMINAR ELEMENTOS
frutas = ["Mango", "Manzana", "Plátano", "Kiwi", "Melocotón", "Cereza"]
print(frutas)

#POP() -> me elimina y retorna el elemento eliminado 
frutas.pop() #si no le paso ningun indice, me elimina el ultimo elemento
print(frutas)

frutaEliminada = frutas.pop(0)
print(frutas)
print(frutaEliminada)

#REMOVE()
frutas.remove("Melocotón")
print(frutas)

#DEL
del frutas[0]
print(frutas)

indice = frutas.index("Plátano")
print(indice)
'''

'''
#CONVERTIR UN TEXTO EN LISTA
texto = "Hola que tal"
lista_palabras = (texto.split())
print(lista_palabras)
'''
'''
ENUNCIADO: TENEMOS UN TEXTO DÓNDE QUEREMOS ENCONTRAR PALABRAS CLAVE. 
LAS PALABRAS CLAVE PUEDEN SER HASTA 5 Y DEBEREMOS PEDÍRSELAS AL USUARIO 
Y GUARDARLAS EN UNA LISTA. SI EL USUARIO QUIERE PONER MENOS DE 5 PALABRAS CLAVE, 
EBERÁ ESCRIBIR "FIN" PARA TERMINAR DE INTRODUCIR DATOS. SI EL USUARIO INTRODUCE 
NÚMEROS O NADA, DEBEREMOS ELIMINARLOS DE LA LISTA ANTES DE LA BÚSQUEDA.
EN OTRA LISTA, DEBEREMOS GUARDAR EL NÚMERO DE VECES QUE APARECE CADA 
PALABRA CLAVE EN NUESTRO TEXTO. POR EJEMPLO, SI LAS PALABRAS CLAVE SON
ORDENADOR Y PORTÁTIL Y APARECEN 5 Y 7 VECES RESPECTIVAMENTE, NUESTRAS LISTAS
DEBERÍAN SER ASÍ: 
    -   KEYWORDS = ["ORDENADOR", "PORTÁTIL"]
    -   OCURRENCIAS = [5, 7]
'''

texto = """"Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada. 
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior. 
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar. 
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar. 
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas.""" 

keywords = []
keywords_repeat = []

for x in range(5):
    keyword = input("Introduce una palabra clave o 'fin' para terminar: ")
    if keyword == 'fin':
        break
    else:
        keywords.append(keyword)

print(keywords)

posicion = 0
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '': #EMPTY
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion +=1    
print("Lista de keywords corregida")   
print(keywords)

texto = texto.replace('.', '').replace(',', '').split()

longitud_keywords = len(keywords)
for x in range(longitud_keywords):
    keywords_repeat.append(0)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            keywords_repeat[pos] += 1
            break
print(keywords_repeat)  