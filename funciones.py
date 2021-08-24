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
#SOLUCIÓN



def sumar(n1, n2):
    print("Resultado de la suma: "+ str(n1+n2))

def restar(n1, n2):
    print("Resultado de la resta: "+ str(n1-n2))

def dividir(n1, n2):
    if(n2 == 0):
        print("No puedo dividir entre 0")
    else:
        print("Resultado de la division: "+ str(n1/n2))

def multiplicacion(n1, n2):
    print("Resultado de la multiplicacion: "+ str(n1*n2))


print("""Calduladora
-------------
1.Sumar
2.Restar
3.Dividir
4.Multiplicar""")

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
opcion = int(input("Que calculo quiere hacer? "))


if (opcion == 1):
    sumar(numero1, numero2)
elif (opcion == 2):
    restar(numero1, numero2)
elif (opcion == 3):
    dividir(numero1, numero2)
else:
    multiplicacion(numero1, numero2)    