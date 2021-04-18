#Las Tuplas son colecciones de datos ordenadas e inmutables.
#Se puede pensar en ellas como listas inmutables.
miTupla = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(miTupla)

miLista = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(miLista)

#Crear una tupla vacía
tuplaVacia = ()
print(type(tuplaVacia))

#Tupla de un solo elemento
tuplaUnElemento = ("uno", )    # paréntesis y coma
tuplaUnElemento2 = "uno",     # sin paréntesis, solo la coma

miTup1 = 1, 
print(type(miTup1))    # salida: <class 'tuple'>

miTup2 = 1
print(type(miTup2))    # salida: <class 'int'>

#Acceder los elementos de la tupla al indexarlos
print(miTupla[4])    # salida: (3, 4)

#Eliminar la tupla completa
tuplaDel = 1, 2, 3, 
del tuplaDel
print()

#Puedes navegar a través de los elementos de una tupla con un bucle (Ejemplo 1)
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

#Verificar si un elemento o no esta presente en la tupla (Ejemplo 2)
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

#Emplear la función len() para verificar cuantos elementos existen en la tupla (Ejemplo 3)
t3 = (1, 2, 3, 5)
print(len(t3))

#Unir o multiplicar tuplas (Ejemplo 4)
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)
print()

#Crear una tupla utilizando la función integrada de Python "tuple()".
#Convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla
miTup = tuple((1, 2, "cadena"))
print(miTup)

lst = [2, 4, 6]
print(lst)    # salida: [2, 4, 6]
print(type(lst))    # salida: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # salida: <class 'tuple'>
print()

#Función integrada de Python denominada "list()"
tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    # outputs: <class 'list'>