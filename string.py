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