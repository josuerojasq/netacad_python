#Puedes emplear la palabra clave "return" para decirle a una función que devuelva algún valor.
#La instrucción "return" termina la función
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # salida: 12

#El resultado de una función se puede asignar fácilmente a una variable
def deseos():
    return "¡Felíz Cumpleaños!"

d = deseos()
print(d)    # salida: ¡Felíz Cumpleaños!

# Ejemplo 1
def deseos2():
    print("Mis deseos")
    return "¡Felíz Cumpleaños!"

deseos2()    # salida: Mis deseos

# Ejemplo 2
print(deseos2())    # salidas: Mis Deseos
                   #          ¡Feliz Cumpleaños!

#Puedes usar una lista como argumento de una función
def HolaaTodos(myList):
    for nombre in myList:
        print("Hola,", nombre)

HolaaTodos(["Adam", "John", "Lucy"])

#Una lista también puede ser un resultado de función
def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))

#Ejercicio 1
def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False 
    
print(isInt(5))
print(isInt(5.0))
print(isInt("5"))

#Ejercicio 2
def evenNumLst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(evenNumLst(11))

#Ejercicio 3
def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l))