#El nombre de una variable ordinaria es el nombre de su contenido.
#El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.
#La asignación: lista2 = lista1 copia el nombre de la matriz, no su contenido.
#En efecto, los dos nombres (lista1 y lista2) identifican la misma ubicación en la memoria de la computadora.
#Modificar uno de ellos afecta al otro, y viceversa.
lista1 = [1]
lista2 = lista1
lista1[0] = 2
print(lista2)

#Una rodaja es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista,
#o partes de una lista.
#miLista[inicio:fin]

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

#Rodajas - índices negativos
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [1:-1]
print(nuevaLista)#El resultado del fragmento es: [8, 6, 4].

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [-1:1]
print(nuevaLista)#La salida del fragmento es: [].

#Si omites "inicio" en tu rodaja, se supone que deseas obtener un segmento que
#comienza en el elemento con índice "0".
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista [:3]
print(nuevaLista)#Es por esto que su salida es: [10, 8, 6].

#Si omites el "fin" en tu rodaja, se supone que deseas que
#el segmento termine en el elemento con el índice "len(miLista)".
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[3:]
print(nuevaLista)#Por lo tanto, la salida es: [4, 2].

#El omitir "inicio" y "fin" hace una copia de toda la lista:
miLista = [10, 8, 6, 4, 2]
nuevLista = miLista[:] 
print(nuevLista)#El resultado del fragmento es: [10, 8, 6, 4, 2].

#La instrucción "del" puede eliminar más de un elemento de la lista a la vez,
#también puede eliminar rodajas.
#Nota: En este caso, la rodaja ¡no produce ninguna lista nueva!
miLista = [10, 8, 6, 4, 2]
del miLista[1:3] 
print(miLista)#La salida del fragmento es:[10, 4, 2].

#También es posible eliminar todos los elementos a la vez:
miLista = [10, 8, 6, 4, 2]
del miLista[:] 
print(miLista)#La lista se queda vacía y la salida es: [].

#Al eliminar la rodaja del código, su significado cambia dramáticamente.
miLista = [10, 8, 6, 4, 2]
del miLista 
#print(miLista)  provocará un error de ejecución.
#La instrucción "del" eliminará la lista, no su contenido.