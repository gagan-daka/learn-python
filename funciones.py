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

#FUNCIONES QUE RETORNAN VARIOS VALORES
def sumaYresta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado1, resultado2 = sumaYresta(100, 60)
print("Los resultados son: \nSuma: " + str(resultado1) + "\nResta: "+ str(resultado2))

#   EJERCICIO 1: FUNCIÓN MÁXIMO -> DADOS DOS NÚMEROS, LA FUNCIÓN DEBE ENCONTRAR CUÁL DE LOS DOS
#   ES EL MÁS GRANDE Y RETORNARLO.EXTRA: SE DEBEN COMPROBAR QUE LOS ARGUMENTOS DE LA FUNCIÓN SEAN
#   DE TIPO INT O FLOAT. SI ALGUNO DE LOS DOS NO LO ES, MOSTRAR UN MENSAJE DE ERROR Y RETORNAR FALSE.
#   #SOLUCIÓN


#   EJERCICIO 2: MINI CALCULADORA. PEDIRLE AL USUARIO UNA OPERACIÓN Y DOS NÚMEROS. 
#   LAS OPERACIONES PUEDEN SER SUMA, RESTA, POTENCIA. SI INTRODUCE UNA OPERACIÓN DIFERENTE
#   A ESTAS, MOSTRAR UN MENSAJE DE ERROR. SI LA OPERACIÓN ES CORRECTA, MOSTRAR EL RESULTADO.