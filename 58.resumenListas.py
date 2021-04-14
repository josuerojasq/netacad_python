#La "lista" es un tipo de dato en Python que se utiliza para almacenar múltiples objetos.
#Es una colección ordenada y mutable de elementos separados por comas entre corchetes
miLista  = [1, 1, None, True, 'Soy una cadena', 256, 0]
print (miLista)

#Las listas se pueden indexar y actualizar
print(miLista [4]) # salida: soy una cadena
print(miLista  [-1]) # salida: 0

miLista  [1] = '?'
print (miLista) # salida: [1, '?', None, True, 'Soy una cadena', 256, 0]

miLista.insert (0, "first")
miLista.append ("last")
print (miLista ) # salida: ['first', 1, '?', None, True, 'Soy una cadena', 256, 0, 'last']

#Las listas pueden estar anidadas
miLista = [1, 'a', ["lista", 64, [0, 1], False]]
print(miLista)

#Los elementos de la lista y las listas se pueden eliminar
miLista = [1, 2, 3, 4]
del miLista[2]
print(miLista) # salida: [1, 2, 4]

del miLista  # borra toda la lista

#Las listas pueden ser iteradas mediante el uso del bucle "for"
miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in miLista :
    print(color)

#La función "len()" se puede usar para verificar la longitud de la lista
miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(miLista)) # la salidas es 5

del miLista[2]
print (len(miLista)) # la salidas es 4 

#Ejercicio 1
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)

#Ejercicio 2
lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst)
print(lst2)

#Ejercicio 3
lst = []
del lst
#print(lst) Esto generaria un error!

#Ejercicio 4
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst)) 