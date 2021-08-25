#LISTAS
'''
numeros = [1, 2, 3, 4, 5, 6]
print(numeros)
print(numeros[0])
print(numeros[3])

print(len(numeros))

text = ["A", "B", "C"]
print(text)
print(text[2])
print(text[len(text) - 1]) # NOS DEVUELVE LA ÚLTIMA POSICIÓN

variada = [1, 2, 3, 4.2, False, "Hey"]
print(variada)
'''

#BUCLE FOR
'''
#NORMAL
for variable in range(5):
    print(variable)
'''
'''
#INICIO-FIN
for variable in range(6, 10):
    print(variable)
'''
'''
#INICIO-FIN-SALTO
for variable in range(5, 21, 2):
    print(variable)
'''
'''
#EJEMPLO 1
palabra = "One Piece"
for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(str(letra.upper()) + "-es una vocal")
    elif (letra == " "):
        pass
    else:
        print(str(letra.upper())+"-es una consonante")        
'''

#ITERAR SOBRE UNA LISTA
'''
numeros = [60, 7, 90, 85]
for numero in numeros:
    print(numero)
    numero +=10
    print(numero)

print(numeros)    

for indice in range(len(numeros)):
    numeros[indice]+=10

print(numeros)
'''

#WHILE
'''
contador = 0
while (contador <= 5):
    print(contador)
    contador += 1
'''
'''
#EJEMPLO
letra_encontrada = False
letra = "a"
frase = "Estoy buscando la letra a"
indice = 0

while(not(letra_encontrada)):
    if (frase[indice] == letra):
        letra_encontrada = True
        print(f"Ya hemos encontrado la letra '{letra}', se encuentra en el indice {indice}") #format string
    else:
        indice +=1
'''
'''
#BREAK > SALE DEL BUCLE
frase = "Estoy buscando la letra a"
letra = "e"

for caracter in frase:
    if (caracter == letra):
        print(F"Letra '{letra}' encontrada en la posicion {frase.index(letra)}") #index() FIRST SUBSTRING
        break #TODO LO QUE ESTE ABAJO DE 'BREAK' NO SE VA A EJECUTAR
    else:   
        print("Letra no encontrada")
    print(caracter)
'''
'''
#CONTINUE -> NO SALE DEL BUCLE
frase = "Hola, como estas"
letra = "a"
count = 0

for caracter in frase:
    if (caracter == letra):
        count +=1
        print(f"La letra '{letra}' la hemos encontrado {count} veces")
        continue
    print("Hey")
'''

'''
#PASS -> PASA, LO IGNORA
lista = [10, 20, 30, 40, 0]
for num in lista:
    if(num == 10):
        pass
    print(f"El valor de la variable es {num}")


def hijos_zeus(arg1, arg2):
    pass
def dioses_olimpo(arg1, arg2):
    pass
'''

'''
#ELSE
frase = "Todos los caracteres de una frase"
count = 0
for caracter in frase:
    count +=1
    #if (caracter == "l"):
        #break
else:
    print(f"La frase tiene {count} caracteres")
'''

'''
EJERCICIO: EL USUARIO DEBE ADIVINAR UN NÚMERO ENTRE 0 Y 10.
EL PROGRAMA DEBERÁ PEDIR QUE EL USUARIO INTRODUZCA UN NÚMERO
Y DEBE DECIR SI HA ACERTADO, SI EL NÚMERO ES MENOR O MAYOR QUE
EL QUE HA INTRODUCIDO.
'''

numero_adivinar = 7

def pedirYcomprobar(num):
    numUser = int(input("Adivina el número: "))
    if(numUser == numero_adivinar):
        print("Eres un Crack!")
        return True
    elif (numUser > numero_adivinar):
        print("Te has pasado!!!")
        return False
    elif (numUser < numero_adivinar):
        print("El numero es mayor")
        return False
'''
while(True):
    if (pedirYcomprobar(numero_adivinar)):
        break
'''

while(not(pedirYcomprobar(numero_adivinar))):
    pass
else:
    print("Fin del juego")