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
#EJEMPLO 1
palabra = "One Piece"
for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(str(letra.upper()) + "-es una vocal")
    elif (letra == " "):
        pass
    else:
        print(str(letra.upper())+"-es una consonante")        