#1.- REPASO DE CONCEPTOS BÁSICOS
'''
texto = "Hola ¿Qué tal?" #COMILLAS DOBLES
print(texto)

texto = 'Hola ¿Qué tal?' #COMILLAS SIMPLES
print(texto)

comillas_simples = "En Monkey D. Luffy va dir 'Yo sere el futur rei dels piratas!'"
comillas_dobles = 'En Monkey D. Luffy va dir "Yo sere el futur rei dels piratas!"'
print(comillas_simples)
print(comillas_dobles)

string_con_formato = """hey
===========TEXTO FORMATEADO===========
El texto formateado:
    1.- Poner saltos de linia
    2.- Poner Sangrías
Y mostrarlo así por pantalla
""" #PERMITE SALTOS DE LINIA
print(string_con_formato)
'''
'''
valor_entero = 5
valor_decimal = 3.14
valor_booleano = False
print("Tipos de datos originales:")
print(type(valor_entero))
print(type(valor_decimal))
print(type(valor_booleano))

#CONVERTIR DATOS
valor_entero = str(valor_entero)
valor_decimal = str(valor_decimal)
valor_booleano = str(valor_booleano)
print("Tipos de datos modificados:")
print(type(valor_entero))
print(type(valor_decimal))
print(type(valor_booleano))
'''
'''
#LONGITUD DE UN STRINGS
texto = "0123456789"
print("La longitud del esto es: ")
print(len(texto))

#CONCATENAR STRINGS
texto1 = "01234"
texto2 = "56789"
texto3 = "Los valores son: "+ texto1 + texto2
print(texto3)
'''
'''
#2.- LOS STRING SON LISTAS
texto = "0123456789"
primer_caracter = texto[0]
subs_string = texto[1:5] #[INICIO:FIN]

print("El texto original es: "+ texto)
print("El primer valor es: "+ primer_caracter)
print("El substring es: "+ subs_string)

print("El último caracter es: "+ texto[-1])

print("Iteración: ")
for num in texto:
    print("El número actual es: "+ num)
'''

'''
#TENEMOS UN STRING ÚNICAMENTE COMPUESTO POR NÚMEROS ENTEROS.
#DEBEMOS SUMAR SU VALOR UNO A UNO Y MOSTRAR POR PANTALLA LA SUMA TOTAL DE LOS NÚMEROS
# --- SOLUCION --- 
numeros = "9123756359"
total = 0
for num in numeros:
    total += int(num)
else:
    print("El valor total: "+ str(total))
'''    
'''
#3.- FORMAT STRINGS -> NOS PERMITEN GENERAR STRINGS COMBINANDO TEXTO CON OTRAS VARIABLS DE FORMA SENCILLA
cantidad = 5
precio = 1.50

print("Forma cutre: ")
print("Has comprado " + str(cantidad)+ ". Cada garrafa vale: " + str(precio)+ "€. En total son "+ str(cantidad*precio)+ "€.")

print("Forma avanzada: ")
texto = "Has comprado {}. Cada garrafa vale: {}€. En total son: {}€".format(cantidad, precio, cantidad*precio)
print(texto)

print("Forma mucho mas avanzada (y mas limpia ;) ): ")
print(f"Has comprado {cantidad}. Cada garrafa vale: {precio}€. En total son: {cantidad*precio}€")
'''
'''
#MÉTODOS DE STRINGS
#FIND() e INDEX() -> SIRVEN PARA ENCONTRAR CONJUNTOS DE CARACTERES DENTRO DE UN STRING
#COUNT() -> DEVUELVE LA CANTIDAD DE VECES QUE SE ENCUENTRA UN CARACTER EN UN STRING
#SPLIT() -> DIVIDE EL STRING MEDIANTE UN DELIMITADOR Y CONVIERTE CADA DIVISIÓN EN UN ELEMENTO DE LA LISTA
#REPLACE() -> REEMPLAZA UN SUBSTRING POR OTRO
#JOIN() -> UNE UNA LISTA DE STRINGS EN UN ÚNICO STRING MEDIANTE UN CARACTER DETERMINADO. (ES LO CONTRARIO DE SPLIT)

mail = "correo@gmail.com"
posicion = mail.index('@')
print(posicion)

posicion = mail.find('@')
print(posicion)

posicion = mail.find('gmail') #EL METODO 'FIND()' NOS DEVUELVE LA POSICION EN LA QUE EMPIEZA
print(posicion)

posicion = mail.find('*') # EL METODO 'FIND()' SI NO ENCUENTRA EL CARACTER, NOS DEVUELVE UN -1
print(posicion)

#posicion = mail.index('*') #EL METODO 'INDEX()' SI NO ENCUENTRA EL CARACTER, NOS DA ERROR/EXEPCIÓN
print(posicion)

#COUNT()
apariciones = mail.count('r')
print(f"La letra 'r' aparece {apariciones} veces")

#SPLIT()
compra = "chocolate, pan, agua, plátano, verduras"
compra2 = "chocolate pan agua plátano verduras"
lista_compra = compra.split(', ')
lista_compra2 = compra2.split()
print(lista_compra)
print(lista_compra2)

print(f"En la lista de la compra tenemos {len(lista_compra)} elementos ")

#REPLACE()
lista_modificada = compra.replace(', ', ' - ')
print(lista_modificada)

#JOIN()
compra = ' '.join(lista_compra) #NOS DEVUELVE UN STRING
print(compra)
'''

'''
TENEMOS UNAS DESCRIPCIONES DE ALGUNOS PRODUCTOS. EN ELLAS SE INCLUYE EL PRECIO DE 
CADA PRODUCTO. DEBEMOS ENCONTRAR EL PRECIO EN € Y MOSTRARLO POR PANTALLA. EL PRECIO
PUEDE TENER 0, 1 O 2 DECIMALES Y SIEMPRE VA SEGUIDO DEL SÍMBOLO '€'. POR EJEMPLO:
    - 14.99€
    - 5€
    - 4.5€

BONUS: DEBEREMOS MODIFICAR LAS DESCRIPCIONES PARA QUE EL PRECIO SE MUESTRE EN DÓLARES.
LA CONVERSIÓN ES: 1€ = 1.21$. NO HACE FALTA MODIFICAR LA VARIABLE ORIGINAL DE LA DESCRIPCION,
PODEMOS RETORNAR UNA COPIA CON EL PRECIO CONVERTIDO
'''

des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nique valen 89€. Nunca han estado tan rebajadas."
des3 = "¡Tenemos el bambú en oferta! Cómpralo ahora por 1.2€ el kg ¡No la dejes pasar!"

def findPrice(txt):
    txtList = txt.split()
    posicion = -1
    indice = -1
    conversion = 1.21
    for palabra in txtList:
        posicion = palabra.find('€')
        if posicion != -1:
            indice = txtList.index(palabra)
            break
    precio = txtList[indice]
    precio = precio.split('€')[0]
    txtList[indice] = str(float(precio)*conversion) + '$'
    nuevaDescripcion = " ".join(txtList)
    return precio, nuevaDescripcion


precio, descripcion = findPrice(des1)
print(precio)
print(descripcion)

precio, descripcion = findPrice(des2)
print(precio)
print(descripcion)

precio, descripcion = findPrice(des3)
print(precio)
print(descripcion)