#BOOLEANOS, CONDICIONALES Y ENTRADA DE USUARIO
 

# ENTRADA DE DATOS DEL USUARIO. IDENTIFICACION DEL TIPO DE DATOS
"""
edad=input("Cuantos años tienes? ")
tipo_de_dato = type(edad)
print(edad)
print(tipo_de_dato)
"""

#BOOLEANOS, IF
'''
    OPERADORES
        ==  EQUAL
        !=  NOT EQUAL
        >   GREATER TAH
        <   LESS THA
        >=  GREATHER THAN OR EQUAL TO
        <=  LESS THAN OR EQUAL TO
'''
'''
verdadero = True
falso = False

if (verdadero == True):
    print("Es true")

if (falso == True):
    print("Son iguales")

if (falso == False):
    print("Es falso")
'''
'''
#OPERADORES DE COMPARACION, ELIF, ELSE
edad = input("Cuantos años tienes? ")
edad = int(edad) 
if (edad >= 18):
    print("Puedes pasar")
elif (edad<0):
    print("Has introducido una edad negativa")
else:
    print("No puedes pasar")    
'''

#OPERADORES LÓGICOS AND, OR, NOT
'''
edad = input("Cuantos años tienes? ")
edad = int(edad) 
#EJEMPLO 1
if (type(edad) == int):
    if(edad > 120 or edad < 0):
        print("Esto no es possible")
    elif(edad >= 18 and edad < 40):
        print("Puedes entrar a mui club")
    elif (edad >= 15 and edad < 18)    :
        print("No puedes entrar, eres menor de edad")
    else:
        print("No cumples ninguna de las condiciones")    
else:
    print("Solo puedes introducir numeros, letra NO")        
'''

#EJEMPLO 2
'''
if(not(edad <= 18)):
    print("Eres mayor de edad, puedes pasar")
'''

'''
EJERCICIO: COMPROBAR SI EL USUARIO INTRODUCE UN NÚMERO, 
SI NO ES UN NÚMERO INDICAR QUE DEBE INTRODUCIR UN ENTERO. 
SI ES UN NUMERO, DEBEREMOS COMPROBAR SI ES PAR O NO Y NOTIFICARLO AL USUARIO
'''
#SOLUCIÓN
numero = input("Introduce un numero: ")

if(numero.isnumeric()):
    numero = int(numero) 
    if(numero%2 == 0):
        print("Es par")
    else:
        print("Es impar")
else:
    print("Tienes que introducir un numero entero")



