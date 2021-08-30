'''
#DEFINICIÓN DE LAS FUNCIONES
def saludar():
    print("Función para saludar")

saludar()
saludar()
saludar()
'''

'''
#FUNCIONES CON ARGUMENTOS (PARAMETROS)
def saludar(nombre):
    print("Holaa "+ nombre +"! ¿Qué tal?")

saludar("Gagan")  
saludar("Zorro")    
saludar("Luffy")
'''
'''
#FUNCIONES CON RETORNO
def suma(a, b):
    #resultado = a + b
    #return resultado
    return a + b

#valor = suma(10, 5)
valor = suma(35, 5)
print(valor)

def sonIguales(n1, n2):
    return n1 == n2

verdad = sonIguales(3, 3)
verdad = sonIguales(1, 60)
if(verdad): # verdad == True
    print("Son iguales")
else:
    print("Son diferentes")    
print(verdad)
'''
'''
#FUNCIONES CONA RGUMENTOS CON VALOR POR DEFECTO
def saludarPorDefecto(nombre="Nico Robin"):
    print("Hola "+nombre)
saludarPorDefecto()
saludarPorDefecto("Sanji")
'''

'''
#FUNCIONES QUE RETORNAN VARIOS VALORES
def sumaYresta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado1, resultado2 = sumaYresta(100, 60)
print("Los resultados son: \nSuma: " + str(resultado1) + "\nResta: "+ str(resultado2))
'''

'''
EJERCICIO 1: FUNCIÓN MÁXIMO -> DADOS DOS NÚMEROS, LA FUNCIÓN DEBE ENCONTRAR CUÁL DE LOS DOS
ES EL MÁS GRANDE Y RETORNARLO.
EXTRA: SE DEBEN COMPROBAR QUE LOS ARGUMENTOS DE LA FUNCIÓN SEAN 
DE TIPO INT O FLOAT. SI ALGUNO DE LOS DOS NO LO ES, MOSTRAR UN MENSAJE DE ERROR Y RETORNAR FALSE.
'''
'''
#SOLUCIÓN
def maximo(n1, n2):
    if ((type(n1) == int or type(n1) == float) and (type(n2) == int or type(n2) == float)):
        if(n1 == n2):
            print("Los dos numeros son iguales")
            return n1
        elif(n1 > n2):
            print("El maximo es: "+ str(n1))
        else:
            print("El maximo es: "+ str(n2))
    else:
        print("Error! Has introducido los datos incorrectamente")
        return False

maximo(10, 90)
maximo(10, "aaa")
'''


'''
EJERCICIO 2: MINI CALCULADORA. PEDIRLE AL USUARIO UNA OPERACIÓN Y DOS NÚMEROS. 
LAS OPERACIONES PUEDEN SER SUMA, RESTA, POTENCIA. SI INTRODUCE UNA OPERACIÓN DIFERENTE
A ESTAS, MOSTRAR UN MENSAJE DE ERROR. SI LA OPERACIÓN ES CORRECTA, MOSTRAR EL RESULTADO.
'''

'''
#SOLUCIÓN
def calculadora():
    operacion = input("¿Qué operación quieres hacer?Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")
    num1 = float(input("Introduce el primer valor: "))
    num2 = float(input("Introduce el segundo valor: "))
    if(operacion == "suma"):
        print("El resultado es: ", num1 + num2) 
    elif(operacion == "resta"):
        print("El resultado es: ", num1 - num2) 
    elif(operacion == "potencia"):
        print("El resultado es: ", num1**num2) 
    else:
        print("Operación errónea. Las operaciones posibles son:\n-suma\n-resta\n-potencia\n")

print("Apartado 6: Ejercicio 2. Mini calculadora")
calculadora()
'''

'''
--- ARGUMENTOS ARBITRATIOS --- 
LOS ARGUMENTOS ARBITRATIOS SE UTILIZAN CUANDO NO SABEMOS DE FORMA
EXACTA EL NÚMERO DE PARÁMETROS QUE LA FUNCIÓN VA A RECIBIR
'''
'''
#*args->no se cuantos argumentos voy a RECIBIR
#NOS DEVUELVE UNA LISTA
def  maximo(*args):
    maximo = args[0]
    for numero in args[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

print(maximo(1000,100.1, 500.2))
print(maximo(1,2,3))

def  maximo2(listaNumeros):
    maximo = listaNumeros[0]
    for numero in listaNumeros[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

print(maximo2([1000,100.1, 500.2]))
print(maximo2([1,2,3]))
'''
'''
def formatoDescarga(tipo, *args):
    numArgs = len(args)
    if tipo == "video":
        if numArgs == 0:
            print(f"El formato seleccionado es el siguiente:\n-Tipo de archivo: {tipo}")
        elif numArgs == 1:
            print(f"El formato seleccionado es el siguiente:\n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}")
        elif numArgs == 2:
            print(f"El formato seleccionado es el siguiente:\n-Tipo de archivo: {tipo}\n-Resolución: {args[0]}\n-FPS: {args[1]}")
    elif tipo == "audio":
        print(f"El formato seleccionado es el siguiente:\n-Tipo de archivo: {tipo}")
    else:
        print("El formato es incorrecto o no existe")    

formatoDescarga("video", 720)
formatoDescarga("video", 1080, 60)
formatoDescarga("audio")
formatoDescarga("b")
'''
'''
--- KEYWORD ARGUMENTS --- 
PODEMOS PASAR LOS ARGUMENTOS DE UNA FUNCIÓN
MEDIANTE KEYWORDS. DE ESTA FORMA CONSEGUIMOS QUE EL ORDEN DE
LOS ARGUMENTOS SEA INDIFERENTE
'''
'''
def crearPersonaje(clase, raza, nombre):
    print(f"{nombre.upper()} es un {clase} de raza {raza}")

crearPersonaje(nombre="Goku", clase="super sayan", raza="humano")
crearPersonaje("mago", "elfo", "Steve")
'''
'''
--- KEYWORD ARBITRARY ARGUMENTS --- 
SE UTILIZAN CUANDO NO SABEMOS CUÁNTOS ARGUMENTOS DE PALABRA 
CLAVE VAMOS A RECIBIR
'''
'''
#ALGO SIMILAR A DICCIONARIO COMO PARAMETRO
def printKwargs(**kwargs):
    print("\n")
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

printKwargs(nombre="Goku", clase="super sayan", raza="humano", mascota="Dragon", clan="coorporation")  
printKwargs(clase="mago", tipo="elfo")  
'''
'''
COMBINACION DE ARGUMENTOS OBLIGATORIOS CON LOS ARGUMENTOS ARBITRARIOS
Y CON LOS ARGUMENTOS ARBITRARIOS DE PALABRA CLAVE
'''
def crearPersonaje(nombre, *args, **kwargs):
    descripcion = f"### {nombre.upper()} ###\n\n"
    descripcion += "### DESCRIPCIÓN ### \n\n"
    for clave, valor in kwargs.items():
        descripcion += f"-{clave} : {valor}\n"
    descripcion += "### HABILIDADES ###\n\n"
    for skill in args:
        descripcion += f" - {skill}\n"
    return descripcion

personaje = crearPersonaje("A", "ataque fuerte", "tormenta", "salto triple", clase="mago", raza="elfo", mascota="pajaro celestial")
print(personaje)
